import time
import socket

def wait_for(host, port, timeout=30):
    """Počkej, než bude host:port dostupný (max timeout v sekundách)."""
    start = time.time()
    while True:
        try:
            socket.create_connection((host, port), timeout=2)
            return
        except OSError:
            time.sleep(1)
        if time.time() - start > timeout:
            raise TimeoutError(f"Nepodařilo se připojit k {host}:{port} během {timeout}s")

# Počkej na Redis a PostgreSQL
wait_for("redis-db", 6379)
wait_for("postgres-db", 5432)

# Importuj Flask aplikaci až po ověření služeb
from app import app

def test_homepage():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b'N\xc3\xa1v\xc5\xa1t\xc4\x9bva' in response.data  # "Návštěva" jako UTF-8 bajty

def test_tasks_page():
    client = app.test_client()
    response = client.get('/tasks')
    assert response.status_code == 200
    assert b'Seznam \xc3\xbakol\xc5\xaf' in response.data  # "Seznam úkolů"

def test_stats_page():
    client = app.test_client()
    response = client.get('/stats')
    assert response.status_code == 200
    assert 'Statistiky' in response.data.decode('utf-8')