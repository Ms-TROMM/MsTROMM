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

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

# Table styler{
#   id int [pk, increment]
#   water_percentage int [not null]
#   connection int [not null, default:0]
#   dehumidification_connect int [not null, default:0]
#   dry_connect int [not null, default:0]
#   dehumidification int
#   temperature int
# }
