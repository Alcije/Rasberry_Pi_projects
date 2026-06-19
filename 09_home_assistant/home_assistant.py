from pathlib import Path
from flask import Flask, redirect
import RPi.GPIO as GPIO

LED_PIN = 18
TEMP_FILE = Path("/sys/class/thermal/thermal_zone0/temp")

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

app = Flask(__name__)


def cpu_temp():
    try:
        return int(TEMP_FILE.read_text().strip()) / 1000
    except FileNotFoundError:
        return None


@app.route("/")
def home():
    temp = cpu_temp()
    temp_text = "not available" if temp is None else f"{temp:.1f} °C"
    led_text = "ON" if GPIO.input(LED_PIN) else "OFF"

    return f"""
    <h1>Small Raspberry Pi home panel</h1>
    <p>CPU temperature: {temp_text}</p>
    <p>LED state: {led_text}</p>
    <p><a href="/on">LED ON</a> | <a href="/off">LED OFF</a></p>
    """


@app.route("/on")
def turn_on():
    GPIO.output(LED_PIN, GPIO.HIGH)
    return redirect("/")


@app.route("/off")
def turn_off():
    GPIO.output(LED_PIN, GPIO.LOW)
    return redirect("/")


if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0", port=5000)
    finally:
        GPIO.cleanup()
