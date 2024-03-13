import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]

number = [1, 1, 1, 1, 1, 1, 1, 1]

GPIO.setup(dac, GPIO.OUT)
GPIO.output(dac, number)
time.sleep(10)

for i in range(8):
    GPIO.output(dac[i-1], 0)
GPIO.cleanup()

# U(255) = 3.234 В
# U(127) = 1.667 В
# U(64) = 0.864 В
# U(32) = 0.456 В
# U(5) = 113.8 мВ
# U(0) = 49.8 мВ