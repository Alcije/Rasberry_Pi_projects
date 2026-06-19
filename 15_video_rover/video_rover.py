from flask import Flask, Response, redirect
import cv2
import RPi.GPIO as GPIO

LEFT_A = 5
LEFT_B = 6
RIGHT_A = 13
RIGHT_B = 19

GPIO.setmode(GPIO.BCM)
for pin in [LEFT_A, LEFT_B, RIGHT_A, RIGHT_B]:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

camera = cv2.VideoCapture(0)
app = Flask(__name__)


def move(la, lb, ra, rb):
    GPIO.output(LEFT_A, la)
    GPIO.output(LEFT_B, lb)
    GPIO.output(RIGHT_A, ra)
    GPIO.output(RIGHT_B, rb)


def frame_stream():
    while True:
        ok, frame = camera.read()
        if not ok:
            continue

        ok, buffer = cv2.imencode(".jpg", frame)
        if not ok:
            continue

        yield (b"--frame\r\n"
               b"Content-Type: image/jpeg\r\n\r\n" + buffer.tobytes() + b"\r\n")


@app.route("/")
def home():
    return """
    <h1>Video rover</h1>
    <img src="/video" width="480">
    <p><a href="/forward">Forward</a></p>
    <p><a href="/left">Left</a> | <a href="/stop">Stop</a> | <a href="/right">Right</a></p>
    <p><a href="/backward">Backward</a></p>
    """


@app.route("/video")
def video():
    return Response(frame_stream(), mimetype="multipart/x-mixed-replace; boundary=frame")


@app.route("/forward")
def forward():
    move(1, 0, 1, 0)
    return redirect("/")


@app.route("/backward")
def backward():
    move(0, 1, 0, 1)
    return redirect("/")


@app.route("/left")
def left():
    move(0, 1, 1, 0)
    return redirect("/")


@app.route("/right")
def right():
    move(1, 0, 0, 1)
    return redirect("/")


@app.route("/stop")
def stop_route():
    move(0, 0, 0, 0)
    return redirect("/")


if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0", port=5000)
    finally:
        move(0, 0, 0, 0)
        camera.release()
        GPIO.cleanup()
