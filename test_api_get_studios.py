import requests

def test_get():
    url = 'http://127.0.0.1:8000/'
    response = requests.get(url)
    print(response.status_code)
    print(response.json())
    assert response.status_code == 200