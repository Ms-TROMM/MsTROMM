from .. main import db
from marshmallow import Schema, fields


class UserPreference(db.Model):
    __tablename__ = 'user_preference'

    id = db.Column(db.Integer, primary_key=True, default=1, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    scent_id = db.Column(db.Integer, db.ForeignKey('scent.id'), nullable=False)
    fashion_style = db.Column(db.String(30), nullable=True)
    color = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return '<User %r>' % self.username

    def __init__(self, user_id, scent_id, fashion_style, color):
        # enable list of fashion style & color ? 
        self.user_id = user_id
        self.scent_id = scent_id
        self.fashion_style = fashion_style
        self.color = color
        
    def create(self):
        db.session.add(self)
        db.session.commit()
        return self
        
class preferSchema(Schema):
    id = fields.Integer()
    user_id = fields.Integer()
    scent_id = fields.Integer()
    fashion_style = fields.String()
    color = fields.Integer()    
