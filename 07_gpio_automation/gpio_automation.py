import time
import RPi.GPIO as GPIO

PINS = [17, 27, 22]
DELAY = 0.4

GPIO.setmode(GPIO.BCM)

for pin in PINS:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

try:
    print("GPIO sequence started.")
    while True:
        for pin in PINS:
            GPIO.output(pin, GPIO.HIGH)
            time.sleep(DELAY)
            GPIO.output(pin, GPIO.LOW)

except KeyboardInterrupt:
    print("\nSequence stopped.")

finally:
    GPIO.cleanup()
