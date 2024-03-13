import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

leds = [2, 3, 4, 17, 27, 22, 10, 9]
aux = [21, 20, 26, 16, 19, 25, 23, 24]

GPIO.setup(leds, GPIO.OUT)
GPIO.setup(aux, GPIO.IN)

while 1:
    for i in range(8):
        if GPIO.input(aux[i-1]) == 1:
            GPIO.output(leds[i-1], 1)
        else:
            GPIO.output(leds[i-1], 0)