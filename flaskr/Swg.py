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


class HomeInfo:
    specs_dict = {
    "parameters": [
        {
        "name": "HomeInfo",
        "in": "path",
        "type": ["integer","string"],
        "required": "true",
        "default": "Nothing"
        }
    ],
    "definitions" : {
        "HomeInfo": {
        "type": "object",
        "properties": {
            "dehumification_connect": {
                "type": "integer",
            },
            "dry_connection": {
                "type": "integer",
            },
            "indoor_humidity": {
                "type": "integer",
            },
            "indoor_temp": {
                "type": "integer",
            },
            "max_temp": {
                "type": "integer",
            },
            "min_temp": {
                "type": "integer",
            },
            "mirror_connection": {
                "type": "integer",
            },
            "now_mode": {
                "type": "string",
            },
            "now_temp": {
                "type": "integer",
            },
            "styler_connection": {
                "type": "integer",
            },
            "styler_water": {
                "type": "integer",
            },
            "todya_date": {
                "type": "string",
            },
            "today_week": {
                "type": "string",
            },
            "userid": {
                "type": "integer",
            },
            "username": {
                "type": "string",
            },
        }
        },
    },
    "responses": {
    "200": {
        "description": "Show Home Information",
        "schema": {
            "$ref": '#/definitions/HomeInfo', 
            },
        "examples": {
            "dehumification_connect" : 0,
            "dry_connect" : 0,
            "indoor_humidity" : 60,
            "indoor_temp" : 22,
            "max_temp" : 10,
            "min_temp" : 8,
            "mirror_connection" : 0,
            "now_mode" : "리프레쉬",
            "now_temp" : 10,
            "styler_connection" : 1,
            "styler_water" : 100,
            "today_date" : "06",
            "today_week" : "월",
            "userid" : 1,
            "username" : "김엘지"
        }
        }
    }
    }

class ControlRecom:
    specs_dict = {
    "parameters": [
        {
        "name": "ControlRecom",
        "in": "path",
        "type": ["integer","string"],
        "required": "true",
        "default": "Nothing"
        }
    ],
    "definitions" : {
        "ControlRecom": {
        "type": "object",
        "properties": {
            "course": {
                "type": "list",
            },
            "indoor_temp": {
                "type": "string",
            },
            "is_inside_styler": {
                "type": "string",
            },
            "texture": {
                "type": "string",
            },
            "useid": {
                "type": "integer",
            }
        }
        },
    },
    "responses": {
    "200": {
        "description": "Show Control Recommendation",
        "schema": {
            "$ref": '#/definitions/ConrolRecom', 
            },
        "examples": {
            "course" : ["고급의류 코스", "섬세건조 코스", "스팀살균 코스"],
            "indoor_temp" : 22,
            "is_inside_styler" : "정장1",
            "texture" : "울",
            "userid" : 1
        }
        }
    }
    }
