from ..database import db


class User(db.Model):
    """
    table name : user
    table info
    - id : index id
    - username : name of the user
    - email : user email
    - password
    - sex : following ISO/IEC 5218 standard, 0 = Not known, 1 = Male, 2 = Female, 9 = Not applicable.
    - birth_year
    - push : push alarm acceptance status. 0 = rejected, 1 = accepted
    """
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    sex = db.Column(db.Integer, nullable=False)
    birth_year = db.Column(db.Integer, nullable=False)
    push = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return '<User %r>' % self.username

    def __init__(self, username, email, password, sex, birth_year, push):
        self.username = username
        self.email = email
        self.password = password
        self.sex = sex
        self.birth_year = birth_year
        self.push = push

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self
