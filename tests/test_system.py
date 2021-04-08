

def test_post_system(app, test_client):
    base_url = "http://127.0.0.1:5000/system/"
    data = {
        "ph_high": 7,
        "ec_low": 1.4,
        "sensor_interval": 120,
        "check_ec_ph_interval": 1200,
    }
    res = test_client.post(base_url, json=data)
    assert res.status_code == 200


def test_put_system(app, test_client):
    base_url = "http://127.0.0.1:5000/system/1"
    data = {
        "ph_high": 10,
        "ec_low": 1.4,
        "sensor_interval": 120,
        "check_ec_ph_interval": 1300,
    }
    res = test_client.put(base_url, json=data)
    assert res.status_code == 200
