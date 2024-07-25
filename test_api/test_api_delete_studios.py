import requests


def test_delete():
    url = 'http://127.0.0.1:8000/studios/delete'
    del_studio = {
        "studio_name": "My cool Studio"
    }

    response = requests.delete(url, json=del_studio)
    print(response.status_code)
    print(response.json())
    assert response.status_code == 200
