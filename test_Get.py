import json

import requests

def test_get_method():
    head = {
        'Connection': 'keep-alive'
    }

    url = "https://fakerestapi.azurewebsites.net/api/v1/Activities/3"
    response_get = requests.get(url, headers=head)
    print(response_get.status_code)
    # json_response = response_get.json()
    # pretty_response = json.dumps(json_response)
    pretty_response = json.dumps(response_get.json())
    print(pretty_response)
    assert response_get.status_code == 200

