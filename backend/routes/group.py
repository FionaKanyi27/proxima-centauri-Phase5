from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.group import Group
from models.user import User
from schemas.group import GroupSchema
from app import db

class GroupListResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=True)
    parser.add_argument('description', type=str)

    @jwt_required()
    def post(self):
        args = self.parser.parse_args()
        user_id = get_jwt_identity()
        group = Group(name=args['name'], description=args['description'], creator_id=user_id)
        db.session.add(group)
        db.session.commit()
        user = User.query.get(user_id)
        group.members.append(user)
        db.session.commit()
        return GroupSchema().dump(group), 201

    @jwt_required()
    def get(self):
        user_id = get_jwt_identity()
        user = User.query.get(user_id)
        return GroupSchema(many=True).dump(user.groups), 200

class GroupResource(Resource):
    @jwt_required()
    def get(self, group_id):
        group = Group.query.get_or_404(group_id)
        return GroupSchema().dump(group), 200