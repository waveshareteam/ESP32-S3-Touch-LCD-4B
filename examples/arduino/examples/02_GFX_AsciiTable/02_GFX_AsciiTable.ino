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
  Serial.println("Arduino_GFX AsciiTable example");
  Wire.begin(BOARD_I2C_SDA, BOARD_I2C_SCL);

  int charWidth = 8;
  int charHeight = 10;

  int numCols = 480 / charWidth;
  int numRows = 480 / charHeight;

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

  if (!gfx->begin()) {
    Serial.println("gfx->begin() failed!");
  }
  gfx->fillScreen(BLACK);

  gfx->setTextColor(GREEN);
  for (int x = 0; x < numCols; x++) {
    if (x % 4 == 0) {
      gfx->setCursor(10 + x * charWidth, 2);
      gfx->print(x, 16);
    }
  }


  gfx->setTextColor(BLUE);
  for (int y = 0; y < numRows; y++) {
    gfx->setCursor(2, 12 + y * charHeight);
    gfx->print(y, 16);
  }

  char c = 0;
  for (int y = 0; y < numRows; y++) {
    for (int x = 0; x < numCols; x++) {
      gfx->drawChar(10 + x * charWidth, 12 + y * charHeight, c++, WHITE, BLACK);
    }
  }

  delay(5000);
}

void loop() {
}
