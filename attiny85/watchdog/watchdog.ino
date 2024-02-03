/*
 Library: https://github.com/ArminJo/EasyButtonAtInt01
 based on examples/Callback/Callback.ino

*/

#include <Arduino.h>

//#define USE_ATTACH_INTERRUPT // enable it if you get the error " multiple definition of `__vector_1'" (or `__vector_2')

#define USE_BUTTON_0           // Enable code for 1. button at INT0 (pin2)
#include "EasyButtonAtInt01.hpp"

void handleButtonPress(bool aButtonToggleState);    // The button press callback function
void handleButtonRelease(bool aButtonToggleState, uint16_t aButtonPressDurationMillis);
EasyButton Button0AtPin2(&handleButtonPress, &handleButtonRelease); // Button is connected to INT0 (pin2)

#define LED_BUILTIN PB0 // define port of built in LED for your ATtiny
#define ESP_ENABLE PB3  // enable pin for the esp, set high to enable the esp
#define BLINK_SHORT_MILLIS 200
#define BLINK_LONG_MILLIS 600

void setup() {
    pinMode(LED_BUILTIN, OUTPUT);
  
    pinMode(ESP_ENABLE, OUTPUT);

    digitalWrite(ESP_ENABLE, HIGH);

//    pinMode(PB1, OUTPUT);
//    digitalWrite(PB1, LOW);

//    pinMode(PB4, OUTPUT);
//    digitalWrite(PB4, LOW);

//    pinMode(PB5, OUTPUT);
//    digitalWrite(PB5, LOW);

}

void loop() {
    delay(10);
}

void blinkLEDBlocking(uint8_t aLedPin, uint8_t aBlinkCount, uint16_t aDelay) {
    for (int i = 0; i < aBlinkCount; ++i) {

        digitalWrite(LED_BUILTIN, HIGH);
        delay(aDelay);
        digitalWrite(LED_BUILTIN, LOW);
        delay(aDelay);
    }
}

/**
 * The callback function is called at each button press
 * @param aButtonToggleState Initial value is false, so first call is with true
 */
void handleButtonPress(bool aButtonToggleState) {
    digitalWrite(ESP_ENABLE, HIGH);
}

void handleButtonRelease(bool aButtonToggleState, uint16_t aButtonPressDurationMillis) {
    digitalWrite(ESP_ENABLE, LOW);
}
