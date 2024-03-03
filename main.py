from flask import Flask, request, abort
from dotenv import load_dotenv
import os
import requests

load_dotenv()

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return "Hello, this is the home page of the webhook listener.", 200


@app.route("/webhook", methods=["POST"])
def handle_webhook():
    print("Received POST request")
    alert_data = request.data.decode()
    print(f"Received data: {alert_data}")

    bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    message = alert_data
    requests.post(
        f"https://api.telegram.org/bot{bot_token}/sendMessage",
        data={"chat_id": chat_id, "text": message},
    )

    return "", 200


if __name__ == "__main__":
    app.run(port=5000)
