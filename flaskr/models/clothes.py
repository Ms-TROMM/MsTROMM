from ..main import db


class Clothes(db.Model):
    __tablename__ = 'clothes'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    name = db.Column(db.String)
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())
    stylered_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())
    need_styler = db.Column(db.Integer, default=0)
    is_inside_styler = db.Column(db.Integer, default=0)

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self
