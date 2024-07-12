import json
import requests

url = "https://fakerestapi.azurewebsites.net/api/v1/Activities/"
head = {
    'Connection': 'keep-alive',
    'Content-Type': 'application/json'
}
request_payload = {
  "id": 600,
  "title": "testing",
  "dueDate": "2024-07-12T19:08:17.902Z",
  "completed": True
}
def test_post_method():
    response = requests.post(url,
                             headers=head,
                             json=request_payload)
    data = response.json()
    print(response.status_code)
    print(data)

    assert response.status_code == 200
    assert data['id'] == 600



