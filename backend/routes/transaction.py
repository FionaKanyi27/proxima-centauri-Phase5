from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.transaction import Transaction
from models.group import Group
from schemas.transaction import TransactionSchema
from extensions import db

class TransactionListResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('group_id', type=int, required=True)
    parser.add_argument('amount', type=float, required=True)
    parser.add_argument('type', type=str, required=True)

    @jwt_required()
    def post(self):
        args = self.parser.parse_args()
        user_id = int(get_jwt_identity())
        group = Group.query.get_or_404(args['group_id'])
        if user_id not in [member.id for member in group.members]:
            return {'message': 'Not a group member'}, 403
        transaction = Transaction(group_id=args['group_id'], user_id=user_id, amount=args['amount'], type=args['type'])
        db.session.add(transaction)
        db.session.commit()
        return TransactionSchema().dump(transaction), 201

    @jwt_required()
    def get(self):
        user_id = int(get_jwt_identity())
        transactions = Transaction.query.filter_by(user_id=user_id).all()
        return TransactionSchema(many=True).dump(transactions), 200

class TransactionResource(Resource):
    @jwt_required()
    def get(self, transaction_id):
        transaction = Transaction.query.get_or_404(transaction_id)
        return TransactionSchema().dump(transaction), 200