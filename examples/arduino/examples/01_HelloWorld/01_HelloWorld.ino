#include <Arduino.h>
#include "Arduino_GFX_Library.h"
#include "pin_config.h"
#include <Wire.h>

Arduino_XCA9554SWSPI *expander = new Arduino_XCA9554SWSPI(
  BOARD_EXPANDER_LCD_RST,
  BOARD_EXPANDER_LCD_CS,
  BOARD_EXPANDER_LCD_SCL,
  BOARD_EXPANDER_LCD_SDA,
  &Wire,
  BOARD_EXPANDER_ADDRESS);

Arduino_ESP32RGBPanel *rgbpanel = new Arduino_ESP32RGBPanel(
  BOARD_LCD_DE, BOARD_LCD_VSYNC, BOARD_LCD_HSYNC, BOARD_LCD_PCLK,
  BOARD_LCD_R0, BOARD_LCD_R1, BOARD_LCD_R2, BOARD_LCD_R3, BOARD_LCD_R4,
  BOARD_LCD_G0, BOARD_LCD_G1, BOARD_LCD_G2, BOARD_LCD_G3, BOARD_LCD_G4, BOARD_LCD_G5,
  BOARD_LCD_B0, BOARD_LCD_B1, BOARD_LCD_B2, BOARD_LCD_B3, BOARD_LCD_B4,
  1 /* hsync_polarity */, 10 /* hsync_front_porch */, 8 /* hsync_pulse_width */, 50 /* hsync_back_porch */,
  1 /* vsync_polarity */, 10 /* vsync_front_porch */, 8 /* vsync_pulse_width */, 20 /* vsync_back_porch */);
Arduino_RGB_Display *gfx = new Arduino_RGB_Display(
  BOARD_LCD_WIDTH /* width */, BOARD_LCD_HEIGHT /* height */, rgbpanel, 0 /* rotation */, true /* auto_flush */,
  expander, GFX_NOT_DEFINED /* RST */, st7701_type1_init_operations, sizeof(st7701_type1_init_operations));

void setup(void) {
  Serial.begin(115200);
  // Serial.setDebugOutput(true);
  // while(!Serial);
  Serial.println("Arduino_GFX Hello World example");

  Wire.begin(BOARD_I2C_SDA, BOARD_I2C_SCL);

#ifdef GFX_EXTRA_PRE_INIT
  GFX_EXTRA_PRE_INIT();
#endif

  expander->pinMode(BOARD_EXPANDER_TOUCH_RST, OUTPUT);
  expander->pinMode(BOARD_EXPANDER_TOUCH_INT, OUTPUT);
  expander->digitalWrite(BOARD_EXPANDER_TOUCH_INT, LOW);
  delay(200);
  expander->digitalWrite(BOARD_EXPANDER_TOUCH_RST, LOW);
  delay(200);
  expander->digitalWrite(BOARD_EXPANDER_TOUCH_RST, HIGH);
  delay(200);


  // Init Display
  if (!gfx->begin()) {
    Serial.println("gfx->begin() failed!");
  }
  gfx->fillScreen(WHITE);
  gfx->setCursor(10, 10);
  gfx->setTextColor(RED);
  gfx->println("Hello World!");

  delay(2000);  // 5 seconds
}

void loop() {
  gfx->setCursor(random(gfx->width()), random(gfx->height()));
  gfx->setTextColor(random(0xffff), random(0xffff));
  gfx->setTextSize(random(6) /* x scale */, random(6) /* y scale */, random(2) /* pixel_margin */);
  gfx->println("Hello World!");

  delay(200);
}
