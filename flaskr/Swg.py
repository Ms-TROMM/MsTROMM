from flasgger import swag_from
from flask import Flask, jsonify
from flasgger import Swagger


### GET ###
class Status:
    specs_dict = {
    "parameters" : [
        {
        "name" : "device",
        "in" : "path",
        "type" : "string",
        "required" : "true",
        "default" : "styler"
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
        "name": "userid",
        "in": "path",
        "type": "integer",
        "required": "true",
        "default": 1
        },
        {
        "name": "city",
        "in": "path",
        "type": "string",
        "required": "true",
        "default": "Seoul"
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
        "name": "userid",
        "in": "path",
        "type": "integer",
        "required": "true",
        "default": "1"
        }
    ],
    "definitions" : {
        "ControlRecom": {
        "type": "object",
        "properties": {
            "course": {
                "type": "list", ## 오류...
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
            "$ref": '#/definitions/ControlRecom', 
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


class CheckStylerState:
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
        "CheckStylerState": {
        "type": "object",
        "properties": {
            "dry": {
                "type": "integer",
            },
            "mirror_connection": {
                "type": "integer",
            },
            "ready": {
                "type": "integer",
            },
            "refresh": {
                "type": "integer",
            },
            "reserv": {
                "type": "integer",
            },
            "styler_connection": {
                "type": "integer",
            },
            "turn_on": {
                "type": "integer",
            }
        }
        },
    },
    "responses": {
    "200": {
        "description": "Show Styler State",
        "schema": {
            "$ref": '#/definitions/CheckStylerState', 
            },
        "examples": {
            "dry" : 0,
            "mirror_connection" : 0,
            "ready" : 0,
            "refresh" : 0,
            "reserv" : 0,
            "styler_connection" : 1,
            "turn_on" : 0
        }
        }
    }
    }


## 수정필요 (example 포멧 수정...)
class Closet:
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
        "Closet": {
        "type": "object",
        "properties": {
            "id": {
                "type": "integer",
            },
            "is_insider_styler": {
                "type": "integer",
            },
            "name": {
                "type": "string",
            },
            "nee_styler": {
                "type": "integer",
            }
        }
        },
    },
    "responses": {
    "200": {
        "description": "Show closet",
        "schema": {
            "$ref": '#/definitions/Closet', 
            },
        "examples": {
            "id" : 1,
            "is_inside_styler" : 1,
            "name" : "정장1",
            "need_styler" : 0
        }
        }
    }
    }


class Weather:
    specs_dict = {
    "parameters": [
        {
        "name": "city",
        "in": "path",
        "type": "string",
        "required": "true",
        "default": "Seoul"
        }
    ],
    "definitions" : {
        "Weather": {
        "type": "object",
        "properties": {
            "daily": {
                "type": "integer",
            },
            "high_temp": {
                "type": "integer",
            },
            "low_temp": {
                "type": "integer",
            }
        }
        },
    },
    "responses": {
    "200": {
        "description": "Show Weather Information",
        "schema": {
            "$ref": '#/definitions/Weather', 
            },
        "examples": {
            "daily" : 0,
            "high_temp" : 9,
            "low_temp" : 8
        }
        }
    }
    }


class TodayRecom:
    specs_dict = {
    "parameters": [
        {
        "name": "city",
        "in": "path",
        "type": "string",
        "required": "true",
        "default": "Seoul"
        },
        {
        "name": "userid",
        "in": "path",
        "type": "integer",
        "required": "true",
        "default": 1
        }
    ],
    "definitions" : {
        "TodayRecom": {
        "type": "object",
        "properties": {
            "down": {
                "type": "string",
            },
            "scent": {
                "type": "string",
            },
            "top": {
                "type": "string",
            }
        }
        },
    },
    "responses": {
    "200": {
        "description": "Show Today Recommendation",
        "schema": {
            "$ref": '#/definitions/TodayRecom', 
            },
        "examples": {
            "down" : "청바지",
            "scent" : "musk",
            "top" : "패딩"
        }
        }
    }
    }


### POST ###
class AddPrefer:
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
        "AddPrefer": {
        "type": "object",
        "properties": {
            "scentid_one": {
                "type": "string",
            },
            "scentid_two": {
                "type": "string",
            },
            "scentid_three": {
                "type": "string",
            },
            "fashion_one": {
                "type": "string",
            },
            "fashion_two": {
                "type": "string",
            },
            "fashion_three": {
                "type": "string",
            },
            "color_one": {
                "type": "string",
            },
            "color_two": {
                "type": "string",
            },
            "color_three": {
                "type": "string",
            }       
        }
        },
    },
    "requests": {
    "200": {
        "description": "Show Add Prefer",
        "schema": {
            "$ref": '#/definitions/AddPrefer', 
            },
        "examples": {
            "scentid_one" : "woody",
            "scentid_two" : "citrus",
            "scentid_three" : "green",
            "fashion_one" : "relax",
            "fashion_two" : "coat",
            "fashion_three" : "clean",
            "color_one" : "green",
            "color_two" : "yellow",
            "color_three" : "ivory"
        }
        }
    }
    }


class AddClothes:
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
        "AddClothes": {
        "type": "object",
        "properties": {
            "name": {
                "type": "string",
            },
            "category": {
                "type": "string",
            },
            "subtype": {
                "type": "integer",
            },
            "color": {
                "type": "integer",
            },
            "texture": {
                "type": "string",
            }
        }
        },
    },
    "requests": {
    "200": {
        "description": "Show Add Clothes",
        "schema": {
            "$ref": '#/definitions/AddClothes', 
            },
        "examples": {
            "name" : "정장1",
            "categpry" : "onepiece",
            "sub_type" : 3,
            "color" : 292929,
            "texture" : "울"
        }
        }
    }
    }