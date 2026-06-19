from flask import Flask, redirect
import RPi.GPIO as GPIO

LED_PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

app = Flask(__name__)


def page():
    state = "ON" if GPIO.input(LED_PIN) else "OFF"
    return f"""
    <h1>LED web control</h1>
    <p>Current LED state: <strong>{state}</strong></p>
    <p>
        <a href="/on">Turn ON</a> |
        <a href="/off">Turn OFF</a>
    </p>
    """


@app.route("/")
def home():
    return page()


@app.route("/on")
def led_on():
    GPIO.output(LED_PIN, GPIO.HIGH)
    return redirect("/")


@app.route("/off")
def led_off():
    GPIO.output(LED_PIN, GPIO.LOW)
    return redirect("/")


if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0", port=5000)
    finally:
        GPIO.cleanup()
