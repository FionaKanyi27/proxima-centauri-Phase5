import pytest
from create_app import create_app, db
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

def test_create_transaction(client):
    client.post('/api/auth/register', json={'email': 'test@example.com', 'password': 'password123', 'role': 'member'})
    token = client.post('/api/auth/login', json={'email': 'test@example.com', 'password': 'password123'}).json['token']
    client.post('/api/groups', json={'name': 'Test Group', 'description': 'A test group'}, headers={'Authorization': f'Bearer {token}'})
    response = client.post('/api/transactions', json={'group_id': 1, 'amount': 100.0, 'type': 'deposit'}, headers={'Authorization': f'Bearer {token}'})
    assert response.status_code == 201
    assert response.json['amount'] == 100.0