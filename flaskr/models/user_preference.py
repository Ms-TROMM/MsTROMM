from .. main import db
from marshmallow import Schema, fields


class UserPreference(db.Model):
    __tablename__ = 'user_preference'

    id = db.Column(db.Integer, primary_key=True, default=1, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    scent_id_one = db.Column(db.Integer, db.ForeignKey('scent.id'), nullable=False)
    scent_id_two = db.Column(db.Integer, nullable=True)
    scent_id_three = db.Column(db.Integer, nullable=True)
    fashion_style_one = db.Column(db.String(30), nullable=False)
    fashion_style_two = db.Column(db.String(30), nullable=True)
    fashion_style_three = db.Column(db.String(30), nullable=True)
    color_one = db.Column(db.Integer, nullable=False)
    color_two = db.Column(db.Integer, nullable=True)
    color_three = db.Column(db.Integer, nullable=True)
    

    def __repr__(self):
        return '<User %r>' % self.username

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
    scent_id_one = fields.Integer()
    scent_id_two = fields.Integer()
    scent_id_three = fields.Integer()
    fashion_style_one = fields.String()
    fashion_style_two = fields.String()
    fashion_style_three = fields.String()
    color_one = fields.Integer() 
    color_two = fields.Integer() 
    color_three = fields.Integer()