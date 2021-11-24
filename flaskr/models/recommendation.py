from ..database import db


class Recommendation(db.Model):
    __tablename__ = 'recommendation'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    scent_id = db.Column(db.Integer, db.ForeignKey('scent.id'), nullable=False)
    recommendation_type_id = db.Column(db.Integer, db.ForeignKey('recommendation_type.type_id'))
    schedule_id = db.Column(db.Integer, db.ForeignKey('schedule.id'), nullable=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    clothes_combination_id = db.Column(db.Integer, nullable=True)
    control_id = db.Column(db.Integer, nullable=True)
    is_useful = db.Column(db.Integer, nullable=True)

    def __init__(self, user_id, scent_id, recommendation_type_id, schedule_id, title, description,
                 clothes_combination_id, control_id, is_useful):
        self.user_id = user_id
        self.scent_id = scent_id
        self.recommendation_type_id = recommendation_type_id
        self.schedule_id = schedule_id
        self.title = title
        self.description = description
        self.clothes_combination_id = clothes_combination_id
        self.control_id = control_id
        self.is_useful = is_useful

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

# CREATE TABLE recommendation (
#   id INTEGER PRIMARY KEY AUTOINCREMENT, 
#   created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
#   user_id INTEGER NOT NULL,
#   recommendation_type_id INTEGER NOT NULL, 
#   title VARCHAR(100) NOT NULL,
#   description VARCHAR(255) NULL, 
#   schedule_id INTEGER NULL,
#   clothes_combination_id INTEGER NULL,
#   scent_id INTEGER NULL,
#   control_id INTEGER NULL,
#   is_useful SMALLINT NULL, -- useful if 1, otherwise 0 
#   FOREIGN KEY (user_id) REFERENCES user (id),
#   FOREIGN KEY (schedule_id) REFERENCES schedule (id), 
#   FOREIGN KEY (clothes_combination_id) REFERENCES clothes_combination (id),
#   FOREIGN KEY (scent_id) REFERENCES scent (id),
#   FOREIGN KEY (control_id) REFERENCES control (id),
#   FOREIGN KEY (recommendation_type_id) REFERENCES recommendation_type (type_id)
# );
