import enum

from ..main import db


class ClothesType(enum.Enum):
    top = 0
    down = 1
    outwear = 2
    onepiece = 3


class Clothes(db.Model):
    __tablename__ = 'clothes'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    clothes_type = db.Column(db.Enum(ClothesType))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    name = db.Column(db.String)
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())
    stylered_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())
    need_styler = db.Column(db.Integer, default=0) # if the clothes needs to be in styler,
    # this value is set to 1, otherwise 0
    is_inside_styler = db.Column(db.Integer, default=0)
    color = db.Column(db.Integer) # Must convert hexadecimal color value to integer before inserting into database
    texture = db.Column(db.String)

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self
