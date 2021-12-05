from ..main import db


class Scent(db.Model):
    __tablename__ = 'scent'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), nullable=False)
    description = db.Column(db.String(255), nullable=False)

    def __init__(self, name, description):
        self.name = name
        self.description = description
        
    def create(self):
        db.session.add(self)
        db.session.commit()
        return self
