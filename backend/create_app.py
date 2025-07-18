from flask import Flask
from config import Config
from extensions import db, ma, jwt
from flask_restful import Api

def create_app():
    print("Creating Flask app")
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions with the app
    print("Initializing extensions")
    try:
        db.init_app(app)
        ma.init_app(app)
        api = Api(app)  # Initialize API directly with app
        jwt.init_app(app)
    except Exception as e:
        print(f"Error initializing extensions: {e}")
        raise

    # Register routes and models within app context
    with app.app_context():
        print("Entering app context")
        try:
            # Import models to register with SQLAlchemy
            from models.user import User
            from models.group import Group
            from models.transaction import Transaction
            print("Models imported")

            # Import and register routes
            from routes.auth import AuthRegister, AuthLogin
            from routes.group import GroupResource, GroupListResource
            from routes.transaction import TransactionResource, TransactionListResource
            print("Routes imported")

            api.add_resource(AuthRegister, '/api/auth/register')
            api.add_resource(AuthLogin, '/api/auth/login')
            api.add_resource(GroupListResource, '/api/groups')
            api.add_resource(GroupResource, '/api/groups/<int:group_id>')
            api.add_resource(TransactionListResource, '/api/transactions')
            api.add_resource(TransactionResource, '/api/transactions/<int:transaction_id>')
            print("Routes registered")

            # Create database tables
            db.create_all()
            print("Database tables created")

        except Exception as e:
            print(f"Error in app context: {e}")
            raise

    # Debug: Print all registered routes (outside app context)
    print("Registered routes:", [rule for rule in app.url_map.iter_rules()])
    return app