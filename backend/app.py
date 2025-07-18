from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api
from flask_jwt_extended import JWTManager
from config import Config
from routes.auth import AuthRegister, AuthLogin
from routes.group import GroupResource, GroupListResource
from routes.transaction import TransactionResource, TransactionListResource

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(app)
jwt = JWTManager(app)

# Register routes
api.add_resource(AuthRegister, '/api/auth/register')
api.add_resource(AuthLogin, '/api/auth/login')
api.add_resource(GroupListResource, '/api/groups')
api.add_resource(GroupResource, '/api/groups/<int:group_id>')
api.add_resource(TransactionListResource, '/api/transactions')
api.add_resource(TransactionResource, '/api/transactions/<int:transaction_id>')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)