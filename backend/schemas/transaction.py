from app import ma
from models.transaction import Transaction

class TransactionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Transaction