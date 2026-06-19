import RPi.GPIO as GPIO
import time

LED_PIN = 18
BUTTON_PIN = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    print("Button test started. Press Ctrl+C to stop.")
    while True:
        button_pressed = GPIO.input(BUTTON_PIN) == GPIO.LOW

        if button_pressed:
            GPIO.output(LED_PIN, GPIO.HIGH)
        else:
            GPIO.output(LED_PIN, GPIO.LOW)

        time.sleep(0.05)

except KeyboardInterrupt:
    print("\nStopping the program.")

finally:
    GPIO.cleanup()
