import requests

def test_get():
    url = 'http://127.0.0.1:8000/studios'
    response = requests.get(url)
    print(response.status_code)
    print(response.json())
    assert resptest_api.pyonse.status_code == 200