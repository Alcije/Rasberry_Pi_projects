import csv
import time
from pathlib import Path
import RPi.GPIO as GPIO

TRIG = 23
ECHO = 24
LOG_FILE = Path("rover_log.csv")

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)


def read_distance():
    GPIO.output(TRIG, GPIO.LOW)
    time.sleep(0.02)
    GPIO.output(TRIG, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(TRIG, GPIO.LOW)

    start = time.time()
    timeout = start + 0.04
    while GPIO.input(ECHO) == 0 and time.time() < timeout:
        start = time.time()

    stop = time.time()
    timeout = stop + 0.04
    while GPIO.input(ECHO) == 1 and time.time() < timeout:
        stop = time.time()

    return (stop - start) * 34300 / 2


need_header = not LOG_FILE.exists()

try:
    with LOG_FILE.open("a", newline="") as file:
        writer = csv.writer(file)
        if need_header:
            writer.writerow(["time", "distance_cm"])

        print("Rover logger started. Press Ctrl+C to stop.")
        while True:
            distance = read_distance()
            moment = time.strftime("%Y-%m-%d %H:%M:%S")
            writer.writerow([moment, round(distance, 2)])
            file.flush()
            print(moment, f"{distance:.1f} cm")
            time.sleep(1)

except KeyboardInterrupt:
    print("\nLogger stopped.")

finally:
    GPIO.cleanup()
