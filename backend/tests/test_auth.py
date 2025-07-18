import pytest
from create_app import create_app
from extensions import db

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
            db.session.remove()
            db.drop_all()

def test_register(client):
    response = client.post('/api/auth/register', json={'email': 'test@example.com', 'password': 'password123', 'role': 'member'})
    assert response.status_code == 201
    assert response.json['email'] == 'test@example.com'

def test_login(client):
    client.post('/api/auth/register', json={'email': 'test@example.com', 'password': 'password123', 'role': 'member'})
    response = client.post('/api/auth/login', json={'email': 'test@example.com', 'password': 'password123'})
    assert response.status_code == 200
    assert 'token' in response.json