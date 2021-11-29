from __future__ import print_function
from ssl import _create_default_https_context
from typing import KeysView
import urllib.request
import urllib
from numpy import tracemalloc_domain
import requests
import os.path
import connexion
import json
import datetime
from os import environ
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, jsonify
from marshmallow import Schema, fields, pprint
from http import HTTPStatus
from flaskr.settings import CLEARDB_DATABASE_URL
from werkzeug.exceptions import HTTPException
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials


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


# 날씨 api 가져오기
def getWeather(city):
    openweather_api_url = "https://api.openweathermap.org/data/2.5/"
    service_key = environ.get('weatherApiKey')

    # API 요청시 필요한 인수값 정의
    ow_api_url = openweather_api_url + "weather"
    payload = "?q=" + str(city) + "&" + "appid=" + service_key + "&lang=kr"
    url_total = ow_api_url + payload

    # API 요청하여 데이터 받기
    req = urllib.request.urlopen(url_total)
    res = req.readline()
    # 받은 값 JSON 형태로 정제하여 반환
    items = json.loads(res)
    # print("============================")
    # print("도시명 : %r" % items['name'])
    # print("============================")
    # print("날씨 : %r" % items['weather'][0]['main'])
    # print("날씨상세 : %r" % items['weather'][0]['description'])
    # print("============================")
    # print("현재온도 : %r" % str(int(items['main']['temp'])-273.15))
    # print("체감온도 : %r" % str(int(items['main']['feels_like'])-273.15))
    # print("최저온도 : %r" % str(int(items['main']['temp_min'])-273.15))
    # print("최고온도 : %r" % str(int(items['main']['temp_max'])-273.15))
    # print("습도 : %r" % items['main']['humidity'])
    # print("============================")
    return items

@app.route('/weather/<city>',methods = ['GET'])
def weather(city):
    return getWeather(city)

## google calendar API
@app.route('/calendar',methods = ['GET'])
def calendar():
    SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
    creds = None
    
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('calendar', 'v3', credentials=creds)

    # Call the Calendar API
    calendar_id = environ.get('googleCalId')
    time_min = (datetime.date.today() + datetime.timedelta(days=-100)).isoformat() + 'T00:00:00+09:00'
    time_max = (datetime.date.today() + datetime.timedelta(days=100)).isoformat() + 'T23:59:59+09:00'
    max_results = 5
    is_single_events = True
    orderby = 'startTime'
    events_result = service.events().list(calendarId = calendar_id,
                                        timeMin = time_min,
                                        timeMax = time_max,
                                        maxResults = max_results,
                                        singleEvents = is_single_events,
                                        orderBy = orderby
                                        ).execute()
    return json.dumps(events_result, ensure_ascii=False)
    #return jsonify(events_result)


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


@app.route('/')
def root():
    return '<h1>Welcome to ms-tromm API</h1>'


### error handler ###
@app.errorhandler(HTTPException)
def error_handler(e):
    response = e.get_response()

    response.data = json.dumps({
        'code': e.code,
        'msg' : e.name,
        'desc': e.description,
    })
    response.content_type = 'application/json'
    return response


### Word2Vec in Korea ###
import datetime
import urllib.request
from gensim.models.word2vec import Word2Vec
from gensim.models import Word2Vec
import openpyxl
import pandas as pd
def Word2Vec_KOR():
    ### Calendar에서 일정 받아오기 ###
    schedule = calendar()
    items = json.loads(schedule)

    # now = datetime.datetime.now() # 오늘 날짜
    # today = now.strftime('%Y-%m-%d')
    # now_after_3 = now + datetime.timedelta(days=3) # 오늘로 부터 3일 뒤 날짜
    # date = now_after_3.strftime('%Y-%m-%d')

    # for i in range(100): # range 수정 필요
    #     if items['items'][i]['start']['date'] == date:
    #         todo = (items['items'][i]['summary'])

    ### 테스트용 일정 ###
    date = '2021-12-03'
    if items['items'][1]['start']['date'] == date:
       todo = (items['items'][1]['summary']) # todo = 'LG전자 면접'
    
    ### Word2Vec ###
    #dataset = [['실외 액티비티'], ['실내 데이트'], ['피크닉'], ['저녁 모임'], ['비즈니스 미팅'], ['사무실'], ['가족 모임']]
    dataset = [['실외 액티비티'], ['실내 데이트'], ['피크닉'], ['저녁 모임'], ['비즈니스 미팅'], ['사무실'], ['가족 모임'], ['LG전자 면접'], ['회의'], ['서울숲 피크닉'], ['롯데월드'], ['소프트웨어공학 회의']]
    
    check = [''''''+todo+'''''']
    if check not in dataset:
        dataset.append(check)
    
    model = Word2Vec(sentences = dataset, vector_size = 300, window = 10, min_count = 1, workers = 4, sg = 0)
    
    # print(model.wv.vectors.shape)   
    # print(model.wv.similarity('사무실', '서울숲 피크닉'))
    # print(model.wv.most_similar("회의")[0][0])

    ### 유사도가 가장 높은 단어 반환 ###
    data = ['실외 액티비티', '실내 데이트', '피크닉', '저녁 모임', '비즈니스 미팅', '사무실', '가족 모임']
    if todo in data:
        return todo
    todoList = model.wv.most_similar(todo)
    for i in range(len(todoList)):
        for word in data:
            if todoList[i][0]==word:
                return todoList[i][0]
        

@app.route('/recommendScent',methods = ['GET'])
def recommendScent():
    return 