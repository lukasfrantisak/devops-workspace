from app import app

def test_homepage():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert 'Návštěva č.' in response.data.decode('utf-8')

def test_tasks_page():
    client = app.test_client()
    response = client.get('/tasks')
    assert response.status_code == 200
    assert 'Seznam úkolů' in response.data.decode('utf-8')

def test_stats_page():
    client = app.test_client()
    response = client.get('/stats')
    assert response.status_code == 200
    assert 'Statistiky' in response.data.decode('utf-8')