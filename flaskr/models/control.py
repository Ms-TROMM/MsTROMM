from .. main import db


class Control(db.Model):
    __tablename__ = 'control'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    steril = db.Column(db.Integer, default=0)
    store = db.Column(db.Integer, default=0)
    styling = db.Column(db.Integer, default=0)
    highend = db.Column(db.Integer, default=0)
    steam = db.Column(db.Integer, default=0)
    finedry = db.Column(db.Integer, default=0)
    ready = db.Column(db.Integer, default=0)
    refresh = db.Column(db.Integer, default=0)
    dry = db.Column(db.Integer, default=0)
    autodry = db.Column(db.Integer, default=0)
    indoor_dehumification = db.Column(db.Integer, default=0)
    reserv = db.Column(db.Integer, default=0)

    def __init__(self, steril, store, styling, highend, steam, finedry, ready, refresh, dry, autodry, indoor_dehumification, reserv):
        self.steril = steril
        self.store = store
        self.styling = styling
        self.highend = highend
        self.steam = steam
        self.finedry = finedry
        self.ready = ready
        self.refresh = refresh
        self.dry = dry
        self.autodry = autodry
        self.indoor_dehumification = indoor_dehumification
        self.reserv = reserv

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


# Note how we never defined a __init__ method on the User class?
# That’s because SQLAlchemy adds an implicit constructor to all model classes
# which accepts keyword arguments for all its columns and relationships.
# If you decide to override the constructor for any reason,
# make sure to keep accepting **kwargs and call the super constructor with
# those **kwargs to preserve this behavior:
#
# class Foo(db.Model):
#     # ...
#     def __init__(self, **kwargs):
#         super(Foo, self).__init__(**kwargs)
#         # do custom stuff
#
