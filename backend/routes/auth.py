from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token
from models.user import User
from schemas.user import UserSchema
from create_app import db

class AuthRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('email', type=str, required=True)
    parser.add_argument('password', type=str, required=True)
    parser.add_argument('role', type=str, default='member')

    def post(self):
        args = self.parser.parse_args()
        if User.query.filter_by(email=args['email']).first():
            return {'message': 'User already exists'}, 400
        user = User(email=args['email'], role=args['role'])
        user.set_password(args['password'])
        db.session.add(user)
        db.session.commit()
        return UserSchema().dump(user), 201

class AuthLogin(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('email', type=str, required=True)
    parser.add_argument('password', type=str, required=True)

    def post(self):
        args = self.parser.parse_args()
        user = User.query.filter_by(email=args['email']).first()
        if user and user.check_password(args['password']):
            token = create_access_token(identity=user.id)
            return {'token': token}, 200
        return {'message': 'Invalid credentials'}, 401