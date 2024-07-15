import json
import requests

def test_post_json():
    url = "https://reqres.in/"
    endpoint = "api/users"

    head = {
        'Content-Type': 'application/json'
    }

    # body = {
    #     "name": "morpheus",
    #     "job": "Maintenence"
    # }

    payload = open("./body.json")
    json_body = json.load(payload)


    post_response = requests.post(url+endpoint, headers=head, json=json_body)
    '''
    If using data instead of json, then use data=json.dumps(json_body)
    data value can be amnything json, xml, text     
    '''
    pretty_response = json.dumps(post_response.json(), indent=4)
    # print(pretty_response)
    # print(post_response.status_code)

    assert post_response.status_code == 201
    assert json_body['name'] == post_response.json()["name"]

