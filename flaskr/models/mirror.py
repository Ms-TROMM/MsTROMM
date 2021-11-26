from ..main import db
from marshmallow import Schema, fields
from sqlalchemy import *



class Mirror(db.Model):
    __tablename__ = 'mirror'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, default=1)
    connection = db.Column(db.Integer, nullable=False, default=0)
    
    def __init__(self, connection):
        self.connection = connection
              

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

class MirrorSchema(Schema):
    id = fields.Integer()
    connection = fields.Integer()  

# Table Mirror{
#   id int [pk, increment]
#   connection int [not null, default:0]
# }