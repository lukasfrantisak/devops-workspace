# docker-compose-demo/test_app.py

import pytest
from app import app, db, Visitor, Task

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            db.drop_all()
            db.create_all()
        yield client

def test_homepage(client):
    response = client.get('/')
    assert response.status_code == 200
    assert "Flask + Docker is alive" in response.data.decode('utf-8')

def test_visits(client):
    response1 = client.get('/visits')
    assert response1.status_code == 200
    assert "Počet návštěv: 1" in response1.data.decode('utf-8')

    response2 = client.get('/visits')
    assert "Počet návštěv: 2" in response2.data.decode('utf-8')

def test_tasks(client):
    response = client.post('/tasks', data={'description': 'Testovací úkol'}, follow_redirects=True)
    assert response.status_code == 200
    assert "Testovací úkol" in response.data.decode('utf-8')

def test_form(client):
    response = client.post('/form', data={'name': 'Lukáš'})
    assert response.status_code == 200
    assert "Díky, Lukáš!" in response.data.decode('utf-8')