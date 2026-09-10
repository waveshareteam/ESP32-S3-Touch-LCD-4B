#include "pin_config.h"
#include <Wire.h>
#include "Arduino_GFX_Library.h"

#include "ESP_I2S.h"

#include "esp_check.h"
#include "es8311.h"

I2SClass i2s;
#define EXAMPLE_SAMPLE_RATE 16000
#define EXAMPLE_VOICE_VOLUME 90
#define EXAMPLE_MIC_GAIN (es8311_mic_gain_t)(3)
#define TEST_TONE_HZ 440
#define TEST_TONE_AMPLITUDE 2000
#define TEST_TONE_FRAME_SAMPLES 256

static int16_t test_tone_pcm[TEST_TONE_FRAME_SAMPLES * 2];

Arduino_XCA9554SWSPI *expander = new Arduino_XCA9554SWSPI(
  BOARD_EXPANDER_LCD_RST,
  BOARD_EXPANDER_LCD_CS,
  BOARD_EXPANDER_LCD_SCL,
  BOARD_EXPANDER_LCD_SDA,
  &Wire,
  BOARD_EXPANDER_ADDRESS);

esp_err_t es8311_codec_init(void) {
  es8311_handle_t es_handle = es8311_create(0, ES8311_ADDRRES_0);
  ESP_RETURN_ON_FALSE(es_handle, ESP_FAIL, "ES8311", "create failed");

  const es8311_clock_config_t es_clk = {
    .mclk_inverted = false,
    .sclk_inverted = false,
    .mclk_from_mclk_pin = true,
    .mclk_frequency = EXAMPLE_SAMPLE_RATE * 256,
    .sample_frequency = EXAMPLE_SAMPLE_RATE
  };

  ESP_ERROR_CHECK(es8311_init(es_handle, &es_clk, ES8311_RESOLUTION_16, ES8311_RESOLUTION_16));
  ESP_ERROR_CHECK(es8311_sample_frequency_config(es_handle, es_clk.mclk_frequency, es_clk.sample_frequency));
  ESP_ERROR_CHECK(es8311_microphone_config(es_handle, false));
  ESP_ERROR_CHECK(es8311_voice_volume_set(es_handle, EXAMPLE_VOICE_VOLUME, NULL));
  ESP_ERROR_CHECK(es8311_microphone_gain_set(es_handle, EXAMPLE_MIC_GAIN));
  return ESP_OK;
}

void audio_task(void *param) {
  i2s.setPins(PIN_ES7210_BCLK, PIN_ES7210_LRCK, PIN_ES8311_DOUT, PIN_ES7210_DIN, PIN_ES7210_MCLK);
  if (!i2s.begin(I2S_MODE_STD, EXAMPLE_SAMPLE_RATE, I2S_DATA_BIT_WIDTH_16BIT, I2S_SLOT_MODE_STEREO, I2S_STD_SLOT_BOTH)) {
    Serial.println("I2S init failed!");
    vTaskDelete(NULL);
  }

  if (es8311_codec_init() != ESP_OK) {
    Serial.println("ES8311 init failed!");
    vTaskDelete(NULL);
  }

  uint32_t phase = 0;
  const uint32_t phase_step = (uint32_t)(((uint64_t)TEST_TONE_HZ << 32) / EXAMPLE_SAMPLE_RATE);
  while (1) {
    for (size_t i = 0; i < TEST_TONE_FRAME_SAMPLES; ++i) {
      phase += phase_step;
      int16_t sample = (phase & 0x80000000U) ? TEST_TONE_AMPLITUDE : -TEST_TONE_AMPLITUDE;
      test_tone_pcm[i * 2] = sample;
      test_tone_pcm[i * 2 + 1] = sample;
    }
    i2s.write((uint8_t *)test_tone_pcm, sizeof(test_tone_pcm));
    vTaskDelay(1);
  }
}

void setup() {
  Serial.begin(115200);
  Wire.begin(BOARD_I2C_SDA, BOARD_I2C_SCL);

  expander->pinMode(BOARD_EXPANDER_AMP_CTRL, OUTPUT);
  expander->digitalWrite(BOARD_EXPANDER_AMP_CTRL, HIGH);
  delay(200);

  xTaskCreatePinnedToCore(audio_task, "audio_task", 4096, NULL, 1, NULL, 1);

  Serial.println("Setup complete.");
}

void loop() {
}
