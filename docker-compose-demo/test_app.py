# docker-compose-demo/test_app.py

import pytest
from app import app, db, Task

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_homepage(client):
    response = client.get('/')
    assert response.status_code == 200
    assert "Flask + Docker is alive" in response.data.decode("utf-8")

def test_visits(client):
    response1 = client.get('/visits')
    assert response1.status_code == 200
    assert "Počet návštěv: 1" in response1.data.decode("utf-8")

    response2 = client.get('/visits')
    assert "Počet návštěv: 2" in response2.data.decode("utf-8")

def test_tasks(client):
    # Pošli POST požadavek pro přidání úkolu
    response = client.post('/tasks', data={'description': 'Napsat test'}, follow_redirects=True)
    assert response.status_code == 200
    assert "Napsat test" in response.data.decode("utf-8")

def test_form(client):
    # Odeslání jména přes formulář
    response = client.post('/form', data={'name': 'Lukáš'})
    assert response.status_code == 200
    assert "Díky, Lukáš!" in response.data.decode("utf-8")