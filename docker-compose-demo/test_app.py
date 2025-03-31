from app import app

def test_homepage():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b'Návštěva č.' in response.data

def test_tasks_page():
    client = app.test_client()
    response = client.get('/tasks')
    assert response.status_code == 200
    assert b'Seznam úkolů' in response.data

def test_stats_page():
    client = app.test_client()
    response = client.get('/stats')
    assert response.status_code == 200
    assert b'Statistiky' in response.data