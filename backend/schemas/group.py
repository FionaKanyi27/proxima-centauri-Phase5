from app import ma
from models.group import Group
from schemas.user import UserSchema

class GroupSchema(ma.SQLAlchemyAutoSchema):
    members = ma.Nested(UserSchema, many=True)
    class Meta:
        model = Group