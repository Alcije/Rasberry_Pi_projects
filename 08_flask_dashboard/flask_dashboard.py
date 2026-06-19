from datetime import datetime
import random
from flask import Flask

app = Flask(__name__)


@app.route("/")
def dashboard():
    # Fake values for testing the page before adding real sensors.
    temperature = random.randint(19, 28)
    humidity = random.randint(40, 70)
    now = datetime.now().strftime("%H:%M:%S")

    return f"""
    <h1>Raspberry Pi Dashboard</h1>
    <p>Last update: {now}</p>
    <p>Temperature: {temperature} °C</p>
    <p>Humidity: {humidity} %</p>
    <p>Refresh the page to generate new test values.</p>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
