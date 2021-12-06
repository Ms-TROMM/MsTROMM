from flasgger import swag_from
from flask import Flask, jsonify
from flasgger import Swagger


class Status:
    specs_dict = {
    "parameters" : [
        {
        "name" : "device",
        "in" : "path",
        "type" : "string",
        "required" : "true",
        "default" : "device not found"
        }
    ],
    "definitions" : {
        "DeviceStatus" : {
        "type": "object",
        "properties" : {
            "connection": {
                "type" : "integer",
            },
            "id":{
                "type" : "integer",
            }
        }
        },
    },
    "responses": {
    "200": {
        "description": "Show device status",
        "schema": {
            "$ref": '#/definitions/DeviceStatus', 
            },
        "examples": {
            "connection" : 0,
            "id" : 1
        }
        }
    }
    }
    

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
    "definitions" : {
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