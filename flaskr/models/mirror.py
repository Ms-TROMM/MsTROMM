from ..main import db


class Mirror(db.Model):
    __tablename__ = 'mirror'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    connection = db.Column(db.Integer, nullable=False, default=0)

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

# Table Mirror{
#   id int [pk, increment]
#   connection int [not null, default:0]
# }