from ..main import db


class ClothesCombination(db.Model):
    __tablename__ = 'clothes_combination'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    top_clothes_id = db.Column(db.Integer, db.ForeignKey('clothes.id'), nullable=False)
    down_clothes_id = db.Column(db.Integer, db.ForeignKey('clothes.id'), nullable=False)
    onepiece_clothes_id = db.Column(db.Integer, db.ForeignKey('clothes.id'), nullable=False)
    outwear_clothes_id = db.Column(db.Integer, db.ForeignKey('clothes.id'), nullable=False)

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self
