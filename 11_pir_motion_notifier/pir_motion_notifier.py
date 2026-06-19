import time
import RPi.GPIO as GPIO

PIR_PIN = 24
LED_PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)

last_message_time = 0
cooldown = 3

try:
    print("PIR sensor ready. Waiting for movement...")
    while True:
        movement = GPIO.input(PIR_PIN) == GPIO.HIGH

        if movement:
            GPIO.output(LED_PIN, GPIO.HIGH)
            now = time.time()
            if now - last_message_time > cooldown:
                print("Movement detected.")
                last_message_time = now
        else:
            GPIO.output(LED_PIN, GPIO.LOW)

        time.sleep(0.1)

except KeyboardInterrupt:
    print("\nMotion notifier stopped.")

finally:
    GPIO.cleanup()
