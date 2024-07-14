import requests

def test_auth_token():
    url = "https://gorest.co.in/public/v2/users"
    head = {
        'Connection': 'keep-alive',
        'Authorization': "Bearer 804c0d14a1e972052826f516528c238be06e038aeaa37df003a15fb2f261972b"
    }
    body_post = {
        "name": "niranjan namkeen",
        "email": "namkeeN_niranjan@ryan-rutherford.example",
        "gender": "male",
        "status": "active"
    }

    post_reponse = requests.post(url, headers=head, json=body_post)
    print(post_reponse.status_code)
    post_output = post_reponse.json()
    print(post_output)
    assert post_reponse.status_code == 201

    print("------------------- GET Reuqest ----------------")

    get_response = requests.get(url + '/' + str(post_output["id"]), headers=head)
    print(get_response.status_code)
    assert get_response.status_code == 200


