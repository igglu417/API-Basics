import json
import pytest
import requests

def test_param():
    url = "https://gorest.co.in"
    endpoint = "/public/v2/users"

    para = {
        'page': 3,
        'per_page': 4
    }

    get_response = requests.get(url + endpoint, params=para)
    pretty_response = json.dumps(get_response.json(), indent=4)
    print(pretty_response)
    assert get_response.status_code == 200

