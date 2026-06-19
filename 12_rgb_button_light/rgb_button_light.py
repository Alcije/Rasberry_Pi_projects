import time
import RPi.GPIO as GPIO

RED = 17
GREEN = 27
BLUE = 22
BUTTON = 23

colors = [
    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 1),
    (1, 1, 0),
    (0, 1, 1),
    (1, 0, 1),
    (0, 0, 0),
]

GPIO.setmode(GPIO.BCM)
for pin in [RED, GREEN, BLUE]:
    GPIO.setup(pin, GPIO.OUT)
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def set_color(rgb):
    GPIO.output(RED, rgb[0])
    GPIO.output(GREEN, rgb[1])
    GPIO.output(BLUE, rgb[2])


index = 0
button_was_down = False

try:
    set_color(colors[index])
    while True:
        button_down = GPIO.input(BUTTON) == GPIO.LOW

        if button_down and not button_was_down:
            index = (index + 1) % len(colors)
            set_color(colors[index])
            time.sleep(0.2)

        button_was_down = button_down
        time.sleep(0.03)

except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()
