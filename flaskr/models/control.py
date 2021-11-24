from ..database import db


class Control(db.Model):
    __tablename__ = 'control'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    steam = db.Column(db.Integer, default=0)
    refresh = db.Column(db.Integer, default=0)
    dehumification = db.Column(db.Integer, default=0)
    indoor_dehumification = db.Column(db.Integer, default=0)

    def __init__(self, steam, refresh, dehumification, indoor_dehumification):
        self.steam = steam
        self.refresh = refresh
        self.dehumification = dehumification
        self.indoor_dehumification = indoor_dehumification

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

# CREATE TABLE control (
#   id INTEGER PRIMARY KEY AUTOINCREMENT, 
#   steam INTEGER NULL DEFAULT 0, 
#   refresh INTEGER NULL DEFAULT 0, 
#   dehumification INTEGER NULL DEFAULT 0, 
#   indoor_dehumification INTEGER DEFAULT 0 
# );
