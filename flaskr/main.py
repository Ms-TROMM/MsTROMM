import connexion
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, jsonify
from marshmallow import Schema, fields, pprint

from flaskr.settings import CLEARDB_DATABASE_URL

connexion_app = connexion.App(__name__, specification_dir='./')

connexion_app.add_api('swagger.yml')

app = connexion_app.app
CORS(app)

# Since you’re not creating an event-driven program, turn this feature off.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# This causes SQLAlchemy to echo SQL statements it executes to the console.
app.config['SQLALCHEMY_ECHO'] = True

# Database URL received from heroku
app.config['SQLALCHEMY_DATABASE_URI'] = CLEARDB_DATABASE_URL

#  The db variable is what’s imported into the build_database.py
#  program to give it access to SQLAlchemy and the database.
db = SQLAlchemy(app)

# This initializes Marshmallow and allows it to introspect the SQLAlchemy components attached to the app.
ma = Marshmallow(app)


########## DO NOT DELETE THESE IMPORT STATEMENTS ###########
from flaskr.models.user import User
from flaskr.models.clothes import Clothes
from flaskr.models.scent import Scent
from flaskr.models.clothes_combination import ClothesCombination
from flaskr.models.control import Control
from flaskr.models.recommendation import Recommendation
from flaskr.models.schedule import Schedule
from flaskr.models.styler_alert import StylerAlert
from flaskr.models.user_preference import UserPreference
from flaskr.models.styler import Styler
from flaskr.models.mirror import Mirror,MirrorSchema
db.create_all()



@app.route('/')
def root():
    return '<h1>Welcome to ms-tromm API</h1>'


@app.route('/connection/mirror',methods = ['GET'])
def connection():
    # 값 넣어주기
    # new_Mirror = Mirror(connection=0).create()
    
    # filtering : id가 100인 쿼리 찾기
    new_Mirror = Mirror.query.filter(Mirror.id == 100).first()
    
    # schema
    schema = MirrorSchema()
    result = schema.dump(new_Mirror)
    return result