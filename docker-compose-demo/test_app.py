# docker-compose-demo/test_app.py

import pytest
from app import app, db, Visitor, Task

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.app_context():
        db.drop_all()
        db.create_all()
    with app.test_client() as client:
        yield client

def test_homepage(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Flask + Docker is alive" in response.data

def test_visits(client):
    response1 = client.get('/visits')
    assert b"Počet návštěv: 1" in response1.data

    response2 = client.get('/visits')
    assert b"Počet návštěv: 2" in response2.data

def test_tasks(client):
    response = client.post('/tasks', data={'description': 'Testovací úkol'}, follow_redirects=True)
    assert response.status_code == 200
    assert b"Testovac" in response.data

def test_form(client):
    response = client.post('/form', data={'name': 'Lukáš'}, follow_redirects=True)
    assert response.status_code == 200
    assert b"D\xedky, Luk" in response.data  # Díky, Lukáš!