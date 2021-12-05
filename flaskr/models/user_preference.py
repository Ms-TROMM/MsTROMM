from .. main import db
from marshmallow import Schema, fields
import enum

'''
FashionStyle:
    no = 15
    relax = 1
    coat = 2
    clean = 3
    athleisure = 4
    street = 5
    modern = 6

LikeColor:
    no = 15
    black = 1
    gray = 2
    navy = 3
    ivory = 4
    white = 5
    green = 6
    red = 7
    lavenda = 8
    yellow = 9

LikeScent:
    no = 15
    citrus = 1
    floral = 2
    fruity = 3
    green = 4
    spicy = 5
    musk = 7
    aromatic = 8
    woody = 6
    
    '''

class UserPreference(db.Model):
    __tablename__ = 'user_preference'

    id = db.Column(db.Integer, primary_key=True, default=1, autoincrement=True)
    user_id = db.Column(db.Integer, nullable=False)
    scent_id_one = db.Column(db.String(100), nullable=False)
    scent_id_two = db.Column(db.String(100), nullable=True)
    scent_id_three = db.Column(db.String(100), nullable=True)
    fashion_style_one = db.Column(db.String(100), nullable=False)
    fashion_style_two = db.Column(db.String(100), nullable=True)
    fashion_style_three = db.Column(db.String(100), nullable=True)
    color_one = db.Column(db.String(100), nullable=False)
    color_two = db.Column(db.String(100), nullable=True)
    color_three = db.Column(db.String(100), nullable=True)
    

    def __init__(self, user_id, scent_id_one, scent_id_two, scent_id_three, fashion_style_one, fashion_style_two, fashion_style_three, color_one, color_two, color_three):
        # enable list of fashion style & color ? 
        self.user_id = user_id
        self.scent_id_one = scent_id_one
        self.scent_id_two = scent_id_two
        self.scent_id_three = scent_id_three
        self.fashion_style_two = fashion_style_two
        self.fashion_style_one = fashion_style_one
        self.fashion_style_three = fashion_style_three
        self.color_one = color_one
        self.color_two = color_two
        self.color_three = color_three
        
    def create(self):
        db.session.add(self)
        db.session.commit()
        return self
        
class preferSchema(Schema):
    id = fields.Integer()
    user_id = fields.Integer()
    scent_id_one = fields.String()
    scent_id_two = fields.String()
    scent_id_three = fields.String()
    fashion_style_one = fields.String()
    fashion_style_two = fields.String()
    fashion_style_three = fields.String()
    color_one = fields.String()
    color_two = fields.String()
    color_three = fields.String()