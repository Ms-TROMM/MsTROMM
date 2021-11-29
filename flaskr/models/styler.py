from marshmallow import Schema, fields
from ..main import db


class Styler(db.Model):
    __tablename__ = 'styler'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    water_percentage = db.Column(db.Integer, nullable=False)
    connection = db.Column(db.Integer, default=0)
    dehumification_connect = db.Column(db.Integer, default=0)
    dry_connect = db.Column(db.Integer, default=0)
    humidity = db.Column(db.Integer, default=0)
    temperature = db.Column(db.Integer)
    
    def __init__(self,water_percentage, connection, dehumification_connect, dry_connect, humidity, temperature) :
        self.water_percentage = water_percentage
        self.connection = connection
        self.dehumification_connect = dehumification_connect
        self.dry_connect = dry_connect
        self.humidity = humidity
        self.temperature = temperature
        

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

class stylerSchema(Schema):
    id = fields.Integer()
    water_percentage = fields.Integer()
    connection = fields.Integer()
    dehumification_connect = fields.Integer()
    dry_connect = fields.Integer()
    humidity = fields.Integer()
    temperature = fields.Integer()
    
# Table styler{
#   id int [pk, increment]
#   water_percentage int [not null]
#   connection int [not null, default:0]
#   dehumidification_connect int [not null, default:0]
#   dry_connect int [not null, default:0]
#   dehumidification int
#   temperature int
# }
