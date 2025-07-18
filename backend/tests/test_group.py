import pytest
from create_app import create_app
from extensions import db
from flask_jwt_extended import create_access_token

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

def test_create_group(client):
    client.post('/api/auth/register', json={'email': 'test@example.com', 'password': 'password123', 'role': 'member'})
    token = client.post('/api/auth/login', json={'email': 'test@example.com', 'password': 'password123'}).json['token']
    response = client.post('/api/groups', json={'name': 'Test Group', 'description': 'A test group'}, headers={'Authorization': f'Bearer {token}'})
    assert response.status_code == 201
    assert response.json['name'] == 'Test Group'

def test_get_groups(client):
    client.post('/api/auth/register', json={'email': 'test@example.com', 'password': 'password123', 'role': 'member'})
    token = client.post('/api/auth/login', json={'email': 'test@example.com', 'password': 'password123'}).json['token']
    client.post('/api/groups', json={'name': 'Test Group', 'description': 'A test group'}, headers={'Authorization': f'Bearer {token}'})
    response = client.get('/api/groups', headers={'Authorization': f'Bearer {token}'})
    assert response.status_code == 200
    assert len(response.json) == 1