from extensions import ma
from models.group import Group

class GroupSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Group
        load_instance = True
        include_fk = True
        include_relationships = True