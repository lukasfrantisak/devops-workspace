# docker-compose-demo/test_app.py

import pytest
from app import app, db, Visitor, Task

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_homepage(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Flask + Docker is alive" in response.data

def test_visits(client):
    db.session.query(Visitor).delete()
    db.session.commit()

    response1 = client.get('/visits')
    response2 = client.get('/visits')

    assert "Počet návštěv:" in response1.data.decode('utf-8')
    assert "Počet návštěv:" in response2.data.decode('utf-8')

    count1 = int(response1.data.decode('utf-8').split(":")[1].strip("</h1> "))
    count2 = int(response2.data.decode('utf-8').split(":")[1].strip("</h1> "))

    assert count2 == count1 + 1

def test_tasks(client):
    db.session.query(Task).delete()
    db.session.commit()

    response = client.post('/tasks', data={'description': 'Testovací úkol'}, follow_redirects=True)
    assert response.status_code == 200
    assert "Testovací úkol" in response.data.decode('utf-8')

def test_form(client):
    response = client.post('/form', data={'name': 'Lukáš'})
    assert "Díky, Lukáš!" in response.data.decode('utf-8')