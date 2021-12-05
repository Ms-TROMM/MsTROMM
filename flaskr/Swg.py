from flasgger import swag_from
from flask import Flask, jsonify
from flasgger import Swagger

class Standard:
    specs_dict = {
    "parameters": [
        {
        "name": "userid",
        "in": "path",
        "type": "integer",
        "required": "true",
        "default": 1
        }
    ],
    "definitions": {
        "Username": {
        "type": "object",
        "properties": {
            "username": {
                "type": "string",
            }
        }
        },
    },
    #### 왜 example 안나옴?
    "responses": {
    "200": {
        "description": "Show username",
        "schema": {
            "$ref": '#/definitions/Username', 
            },
        "examples": {
            "username" : "kim"
        }
        }
    }
    }