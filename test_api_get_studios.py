import requests

def test_post():
    url = 'http://127.0.0.1:8000/studios/post'
    response = requests.get(url)
    print(response.status_code)
    print(response.json())
    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/json'

    data = response.json()
    assert data["studio_name_created"]== "Another cool studio1"