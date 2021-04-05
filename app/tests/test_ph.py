import json


def test_get_ph_by_id(app, test_client):
    base_url = "https://127.0.0.1:5000/ph/1"
    headers = {"content-type": "application/json"}
    res = test_client.get(base_url, headers=headers)
    assert res.status_code == 200
    res_data = json.loads(res.data)
    assert res_data["log_id"] == 1
    assert res_data["ph"] == 6
