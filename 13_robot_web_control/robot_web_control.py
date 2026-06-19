from flask import Flask, redirect
import RPi.GPIO as GPIO

LEFT_A = 5
LEFT_B = 6
RIGHT_A = 13
RIGHT_B = 19

GPIO.setmode(GPIO.BCM)
for pin in [LEFT_A, LEFT_B, RIGHT_A, RIGHT_B]:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

app = Flask(__name__)


def motors(left_a, left_b, right_a, right_b):
    GPIO.output(LEFT_A, left_a)
    GPIO.output(LEFT_B, left_b)
    GPIO.output(RIGHT_A, right_a)
    GPIO.output(RIGHT_B, right_b)


def stop():
    motors(0, 0, 0, 0)


@app.route("/")
def home():
    return """
    <h1>Raspberry Pi robot control</h1>
    <p><a href="/forward">Forward</a></p>
    <p><a href="/left">Left</a> | <a href="/stop">Stop</a> | <a href="/right">Right</a></p>
    <p><a href="/backward">Backward</a></p>
    """


@app.route("/forward")
def forward():
    motors(1, 0, 1, 0)
    return redirect("/")


@app.route("/backward")
def backward():
    motors(0, 1, 0, 1)
    return redirect("/")


@app.route("/left")
def left():
    motors(0, 1, 1, 0)
    return redirect("/")


@app.route("/right")
def right():
    motors(1, 0, 0, 1)
    return redirect("/")


@app.route("/stop")
def stop_route():
    stop()
    return redirect("/")


if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0", port=5000)
    finally:
        stop()
        GPIO.cleanup()
