import time
from rpi_ws281x import *
from LEDController import *
import argparse

LED_COUNT      = 64
LED_PIN        = 18
LED_FREQ_HZ    = 800000
LED_DMA        = 10
LED_BRIGHTNESS = 255
LED_INVERT     = False
LED_CHANNEL    = 0




def colorWipe(strip, color, wait_ms=50):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i,color)
        strip.show()
        time.sleep(wait_ms/1000.0)


def setPixel(strip, color, pixel, wait_ms=50):
    strip.setPixelColor(pixel,color)
    strip.show()
    time.sleep(wait_ms/1000.0)

if __name__ == '__main__':
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    strip.begin()

    try:

        while True:
            for i in range(0,8):
                for j in range(0,8):
                    setPixel(strip, Color(255,0,0),AR2STRIP(i,j),30)

            colorWipe(strip, Color(0,0,0),10)

    except KeyboardInterrupt:
        colorWipe(strip,Color(0,0,0),10)


