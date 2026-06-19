import time
import RPi.GPIO as GPIO

TRIG = 23
ECHO = 24
LEFT_A = 5
LEFT_B = 6
RIGHT_A = 13
RIGHT_B = 19
LIMIT_CM = 25

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

for pin in [LEFT_A, LEFT_B, RIGHT_A, RIGHT_B]:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)


def distance_cm():
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


def motors(la, lb, ra, rb):
    GPIO.output(LEFT_A, la)
    GPIO.output(LEFT_B, lb)
    GPIO.output(RIGHT_A, ra)
    GPIO.output(RIGHT_B, rb)


def forward():
    motors(1, 0, 1, 0)


def turn_right():
    motors(1, 0, 0, 1)


def stop():
    motors(0, 0, 0, 0)


try:
    print("Obstacle avoidance robot started.")
    while True:
        distance = distance_cm()
        print(f"Distance: {distance:.1f} cm")

        if distance < LIMIT_CM:
            stop()
            time.sleep(0.2)
            turn_right()
            time.sleep(0.45)
        else:
            forward()

        time.sleep(0.1)

except KeyboardInterrupt:
    print("\nRobot stopped.")

finally:
    stop()
    GPIO.cleanup()
