import json


def test_get(test_client):
    base_url = "http://127.0.0.1:5000/block/"
    headers = {"content-type": "application/json"}
    res = test_client.get(base_url, headers=headers)
    res_data = json.loads(res.data)
    assert isinstance(res_data["data"], list)
    assert isinstance(res_data["data"][2], int)
