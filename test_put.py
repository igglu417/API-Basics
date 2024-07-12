import json
import requests

def test_get_and_put_method():
    head = {
        'Connection': 'keep-alive'
    }
    url = "https://fakerestapi.azurewebsites.net/api/v1/Activities/12"
    response_get = requests.get(url, headers=head)
    print(response_get.status_code)
    data_get = response_get.json()
    print(data_get)
    assert data_get['id'] == 12

    head_put = {
        'Connection': 'keep-alive',
        'Content-Type': 'application/json'
}

    putPayload = {
          "id": 3456,
          "title": "testing",
          "dueDate": "2024-07-12T19:08:17.902Z",
          "completed": True
}
    response_put = requests.put(url, headers=head_put, json=putPayload)
    data_put = response_put.json()
    print(response_put.status_code)
    print(data_put)
    assert data_put['id'] == putPayload["id"]

