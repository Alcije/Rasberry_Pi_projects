from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <h1>Raspberry Pi Web Server</h1>
    <p>Hello from my Raspberry Pi.</p>
    <p>This is a small Flask page running locally on the board.</p>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
