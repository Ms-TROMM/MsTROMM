from flask import Flask, jsonify
from flask.globals import request
from flasgger import Swagger, SwaggerView, Schema, fields
from flaskr.main import status

class Device(Schema):
    name = fields.Str()
    

class MirrorSchema(Schema):
    id = fields.Integer()
    connection = fields.Integer()  

class stylerSchema(Schema):
    id = fields.Integer()
    water_percentage = fields.Integer()
    connection = fields.Integer()
    dehumification_connect = fields.Integer()
    dry_connect = fields.Integer()
    humidity = fields.Integer()
    temperature = fields.Integer()
    now_mode = fields.String()


class StatusView(SwaggerView):
    parameters = [
        {
            "name": "device",
            "in": "path",
            "type": "string",
            "enum": ["mirror", "styler"],
            "required": True,
            "default": "all"
        }
    ]
    if request.get_json["enum"] == "mirror":
        sch = MirrorSchema
    elif request.get_json["enum"] == "styler":
        sch = stylerSchema    
    responses = {
        200: {
            "description": "Status OK",
            "schema": sch
        }
    }

    def get(self, device):
        """
        Colors API using schema
        This example is using marshmallow schemas
        """
        
        return status(device)

app = Flask(__name__)
swagger = Swagger(app)

app.add_url_rule(
    '/status/<device>',
    view_func=StatusView.as_view('status'),
    methods=['GET']
)
