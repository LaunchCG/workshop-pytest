import requests


def test_post():
    url = 'http://127.0.0.1:8000/disciplines/post'
    post_studio = {
        "discipline_name": "My Cool Discipline",
        "studio_name": "ITSM"
    }

    response = requests.post(url, json=post_studio)
    print(response.status_code)
    print(response.json())
    assert response.status_code == 200
