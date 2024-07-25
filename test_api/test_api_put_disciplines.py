import requests

def test_get():
    url = 'http://127.0.0.1:8000/disciplines/put'
    update_studio = {
        "discipline_name": "My Cool Discipline2",
        "studio_name": "Software Engineering"
    }
    response = requests.put(url, json=update_studio)
    print(response.status_code)
    print(response.json())
    assert response.status_code == 200