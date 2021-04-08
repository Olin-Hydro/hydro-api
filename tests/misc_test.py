import requests


def test_create_system():
    base_url = "http://127.0.0.1:5000/system/"
    headers = {"content-type": "application/json"}
    data = {
        "ph_high": 7,
        "ec_low": 1.4,
        "sensor_interval": 120,
        "check_ec_ph_interval": 1200,
    }
    res = requests.post(base_url, json=data)

if __name__ == "__main__":
    test_create_system()