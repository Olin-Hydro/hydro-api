import json


def test_user_login(app, test_client):
    base_url = "https://127.0.0.1:5000/users/"
    user_data = {"email": "fake_email@mail.net", "password": "password123"}
    headers = {"content-type": "application/json"}
    res = test_client.get(base_url, json=user_data, headers=headers)
    assert res.status_code == 200
    res_data = json.loads(res.data)
    assert res_data["name"] == "Jane Doe"
    assert res_data["permission"] == "user"
    assert res_data["user_id"] == 1
    assert res_data["email"] == "fake_email@mail.net"
