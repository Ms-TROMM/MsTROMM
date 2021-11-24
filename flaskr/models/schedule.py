from ..main import db


class Schedule(db.Model):
    __tablename__ = 'schedule'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String)
    description = db.Column(db.String)
    datetime = db.Column(db.DateTime, nullable=False, server_default=db.func.now())

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self
