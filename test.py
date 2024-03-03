import requests

secret_key = "417b331b2f73baea807edca232ed8691d5afa3fa85bb10e6d0d33980550191b1"


def test_webhook():
    response = requests.post(
        "http://localhost:5000/webhook", headers={"X-Hub-Signature": secret_key}
    )
    print("Status code:", response.status_code)
    print("Response body:", response.text)
    assert response.status_code == 200


test_webhook()
