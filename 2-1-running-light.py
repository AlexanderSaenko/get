import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

leds = [2, 3, 4, 17, 27, 22, 10, 9]

GPIO.setup(leds, GPIO.OUT)

for i in range(8):
    GPIO.output(leds[i-1], 0)

for j in range(240):
    GPIO.output(leds[(j-1) % 8], 0)
    time.sleep(0.2)
    GPIO.output(leds[j % 8], 1)
    time.sleep(0.2)

GPIO.cleanup()