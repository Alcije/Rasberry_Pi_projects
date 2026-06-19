import time
import RPi.GPIO as GPIO

try:
    from mfrc522 import SimpleMFRC522
except ImportError:
    SimpleMFRC522 = None

LOCK_RELAY = 18
ALLOWED_UIDS = {1234567890}  # Replace with ur RFID card UID.

GPIO.setmode(GPIO.BCM)
GPIO.setup(LOCK_RELAY, GPIO.OUT)
GPIO.output(LOCK_RELAY, GPIO.LOW)

if SimpleMFRC522 is None:
    print("Install mfrc522 first: pip install mfrc522")
    GPIO.cleanup()
    raise SystemExit

reader = SimpleMFRC522()

try:
    print("RFID door lock ready.")
    while True:
        uid, text = reader.read()
        print(f"Card detected: {uid}")

        if uid in ALLOWED_UIDS:
            print("Access accepted.")
            GPIO.output(LOCK_RELAY, GPIO.HIGH)
            time.sleep(3)
            GPIO.output(LOCK_RELAY, GPIO.LOW)
        else:
            print("Access refused.")

        time.sleep(1)

except KeyboardInterrupt:
    print("\nDoor lock stopped.")

finally:
    GPIO.output(LOCK_RELAY, GPIO.LOW)
    GPIO.cleanup()
