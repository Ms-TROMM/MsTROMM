from __future__ import print_function
import urllib.request
import urllib
import requests
import os.path
import connexion
import json
import datetime
import openpyxl
import pandas as pd
import numpy as np
from os import environ
from ssl import _create_default_https_context
from typing import KeysView
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, jsonify, make_response
from marshmallow import Schema, fields, pprint
from http import HTTPStatus
from flaskr.settings import CLEARDB_DATABASE_URL
from werkzeug.exceptions import HTTPException
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from collections import Counter
from gensim.models.word2vec import Word2Vec
from gensim.models import Word2Vec
from marshmallow import Schema, fields


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
from flaskr.models.clothes import Clothes, clotheSchema
from flaskr.models.scent import Scent
from flaskr.models.clothes_combination import ClothesCombination
from flaskr.models.control import Control, controlSchema
from flaskr.models.recommendation import Recommendation
from flaskr.models.schedule import Schedule
from flaskr.models.styler_alert import StylerAlert, alertSchema
from flaskr.models.user_preference import UserPreference, preferSchema
from flaskr.models.styler import Styler, stylerSchema
from flaskr.models.mirror import Mirror,MirrorSchema
db.create_all()


#############################################################



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
    # print("도시명 : %r" % items['name'])
    # print("날씨 : %r" % items['weather'][0]['main'])
    # print("날씨상세 : %r" % items['weather'][0]['description'])
    # print("현재온도 : %r" % str(int(items['main']['temp'])-273.15))
    # print("체감온도 : %r" % str(int(items['main']['feels_like'])-273.15))
    # print("최저온도 : %r" % str(int(items['main']['temp_min'])-273.15))
    # print("최고온도 : %r" % str(int(items['main']['temp_max'])-273.15))
    # print("습도 : %r" % items['main']['humidity'])
    return items

## google calendar API
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
    # return events_result
    return json.dumps(events_result, ensure_ascii=False)


class weatherSchema(Schema):
    high_temp = fields.Integer()
    low_temp = fields.Integer()
    daily = fields.Integer()


@app.route('/status/<device>', methods=['GET'])
def status(device):
    new_styler = Styler.query.filter(Styler.id ==1).first()
    new_mirror = Mirror.query.filter(Mirror.id ==1).first()
    print(type(new_mirror))
    schema_st = stylerSchema()
    schema_mi = stylerSchema(only=("id","connection"))
    if device == 'styler':
        result = schema_st.dump(new_styler)
        return result
    elif device == 'mirror':
        result = schema_mi.dump(new_mirror)
        return result
    else:
        return 'device not found'
    

## Add user Prefer
@app.route('/<userid>/preference',methods = ['POST'])
def add_prefer(userid):
    json_data = request.get_json()
    schema = preferSchema()
    new_prefer = UserPreference(user_id=userid, scent_id_one = json_data['scentid_one'],scent_id_two = json_data['scentid_two'], scent_id_three = json_data['scentid_three'],fashion_style_one= json_data['fashion_one'], fashion_style_two= json_data['fashion_two'],fashion_style_three= json_data['fashion_three'], color_one=json_data['color_one'], color_two=json_data['color_two'], color_three=json_data['color_three']).create()
    db.session.commit()
    result = schema.dump(new_prefer)
    return result

    """
    {
"scentid_one":1,
"scentid_two":2,
"scentid_three":3,
"fashion_one":"casual",
"fashion_two":"hip",
"fashion_three":"boxy",
"color_one":292929,
"color_two":292930,
"color_three":292940
}

    """

# Add clothes
@app.route('/<userid>/clothes',methods = ['POST'])
def add_clothes(userid):
    json_data = request.get_json()
    schema = clotheSchema(only=("name","user_id","clothes_type","sub_type","color","texture"))
    new_clothe_data = Clothes(name= json_data['name'],user_id=userid, clothes_type= json_data['category'], sub_type= json_data['sub_type'], color= json_data['color'], texture= json_data['texture'] ).create()
    result = schema.dump(new_clothe_data)
    return result

    """
    {
    "name":"정장1",
    "category":"onepiece",
    "sub_type": 3,
    "color": 292929,
    "texture":"울"
}
    """
    
    
@app.route('/alert/<userid>',methods = ['GET'])  
def alert(userid):
     ### 스타일러 상태 알림(물상태)
     
     ### 오늘의 추천 알림
     
     ### 스타일러 상태 알림(스타일러 가동)
     
     ### 제어 추천 관련 알림
     
     ### 일정 관련 알림
     return '수정중'


@app.route('/recommand/styler/<clothes>',methods = ['GET'])
def need_styler(clothes):
    cal = calendar()
    cal = json.loads(cal)
    cal_li = cal['items'][0:]
    sch_li = [] # 일정 리스트
    sch_date = [] # 일정에 대한 date 리스트
    ## 리스트에 요소 추가
    for i in range(0,len(cal_li)):
        sch_li.append(cal_li[i]['summary'])
        sch_date.append(cal_li[i]['start'])
        
    # 일정에 대한 dict 만들기    
    sch_dict = dict(zip(sch_li,sch_date))
    
    new_clothes = Clothes.query.filter(Clothes.name ==clothes).first()
    schema = clotheSchema()
    clo_json = schema.dump(new_clothes)
    last_time = datetime.date.today() - datetime.date(int(clo_json['stylered_at'][0:4]),int(clo_json['stylered_at'][5:7]),int(clo_json['stylered_at'][8:10])) # 마지막 스타일러 가동으로부터 지난 시간
    
    
    #### 추천 알고리즘(일정 & 마지막 스타일러 가동날짜를 고려한)
    timedel = np.timedelta64(last_time,'ns')
    day = timedel.astype('timedelta64[D]')
    day = day.astype(int)
    
    # sch = Word2Vec_KOR() # if '비즈니스 면접'
    sch = ['피크닉','서울숲 피크닉'] # Word2Vec 결과
    dataset_dict = {'정장':['비즈니스 면접','면접'],'티셔츠':['소풍, 피크닉']} # dataset 업데이트 해야할까?
    event_date = sch_dict[sch[1]]['date'] ## 수정필요 -> 어떻게 서울숲 피크닉을 가져올 것인가?
    new_timedel =  datetime.date(int(event_date[0:4]),int(event_date[5:7]),int(event_date[8:10])) - datetime.date.today()
    new_timedel = np.timedelta64(new_timedel,'ns')
    new_day = new_timedel.astype('timedelta64[D]')
    new_day = new_day.astype(int)
    if sch[0] in dataset_dict[clothes] :
        testing = 1 # 캘린더에 요청한 옷에 관한 스케쥴이 존재
    else :
        testing = 0 # 캘린더에 요청한 옷에 관한 스케쥴 X
        
    if testing == 1:
        tm = 2*day + np.exp2(6-new_day) # 기준 포인트
        ### need_styler_set : 0 = 매우필요 1 = 필요 2 = 괜찮음
        if tm >= 8:
            need_styler_set = 0 # 매우 필요
        
        elif tm >= 6 and tm < 8:
            need_styler_set = 1 # 필요
        
        else :
            need_styler_set = 2 # 괜찮음

    elif testing == 0:
        tm = 2*day + np.exp2(6-new_day) # 기준 포인트
        if tm >= 8:
            need_styler_set = 0 # 매우 필요
        
        elif tm >= 6 and tm < 8:
            need_styler_set = 1 # 필요
        
        else :
            need_styler_set = 2 # 괜찮음


    # need_styler update
    new_clothes.need_styler = need_styler_set
    db.session.commit()
    result = schema.dump(new_clothes)
    return result



@app.route('/control/<userid>/<mode>',methods = ['POST']) ## userid 추가 ?
def control_styler(mode,userid):
    new_styler = Styler.query.filter(Styler.id ==1).first()
    new_control = Control.query.filter(Control.id==1).first()
    schema_sty = stylerSchema()
    schema_con = controlSchema()
    result_con = schema_con.dump(new_control)
    result = schema_sty.dump(new_styler)
    c = Counter(result_con.values())
    
    ## 스타일러 연결 상태 체크
    if result['connection'] == 1:
        
        ##  counter로 1의 갯수를 세서, 기능이 모두 off 일때만 새로운 기능을 on 할 수 있도록
        ## ex. id는 무조건 1이상이므로, 예약을 포함한 작동 중 기능 모두 꺼져 있어야 함
        if c[1] < 2:
            ## 스타일러 모드를 받아와서 실행시킬 모드를 1로 turn on하고 db에 상태 저장
            new_control.data = {mode : 1}
            Control.query.filter_by(id=userid).update(new_control.data)
            db.session.commit()
            update_schema = schema_con.dump(new_control)
            
            ## restful_api로 상태 반환
            return update_schema
        else:
            status = { "status" : 1 } # 스타일러 가동중
            return jsonify(status)
    else:
        conn = { "connection" : 0 } # 스타일러 연결 X
        return jsonify(conn)


@app.route('/control/<userid>',methods = ['GET'])
def control_state(userid):
    conn_dict = {"styler_connection" : Styler.query.filter(Styler.id ==userid).first().connection, "mirror_connection" : Mirror.query.filter(Mirror.id==userid).first().connection}
    new_control = Control.query.filter(Control.id==userid).first()
    schema = controlSchema()
    result = schema.dump(new_control)
    result = {**conn_dict, **result}
    return result


@app.route('/recommand/today/<userid>', methods=['GET'])
def recommand_today(userid):
    name = User.query.filter_by(id=userid).first().username
    info = weatherinfo('Seoul')
    daily = info['daily'] # 일교차: 1 = 큼 / 0 = 크지 않음
    high_temp = info['high_temp'] # 최고기온
    low_temp = info['low_temp'] # 최저기온
    cal = calendar()
    cal = json.loads(cal)
    cal_li = cal['items'][0:]
    sch_li = [] # 일정 리스트
    sch_date = [] # 일정에 대한 date 리스트
    ## 리스트에 요소 추가
    for i in range(0,len(cal_li)):
        sch_li.append(cal_li[i]['summary']) # 스케쥴 리스트
        sch_date.append(cal_li[i]['start']) # 스케쥴 날짜
    
    
    # 이름, 최고온도, 최저온도, 일교차, 스케쥴 리스트
    result = {
        "name":name,
        "max_temp":high_temp,
        "min_temp":low_temp,
        "daily":daily,
        "schedule":sch_li
    }

    return jsonify(result)


@app.route('/recommand/control/<userid>', methods=['GET'])
def recommand_control(userid):
    name = User.query.filter_by(id=userid).first().username
    indoor_temp = Styler.query.filter_by(id=userid).first().temperature
    indoor_humidity = Styler.query.filter_by(id=userid).first().humidity
    inside = Clothes.query.filter(Clothes.is_inside_styler==1).all()
    inside_li = []
    for i in range(0,len(inside)):
        inside_li.append(inside[i].name)
    
    # 이름, 집안 온도, 집안 습도, 스타일러 내 있는 옷
    result = {
        "name":name,
        "indoor_temp":indoor_temp,
        "indoor_humidity":indoor_humidity,
        "inside_list":inside_li
    }
    return jsonify(result)


@app.route('/weather/<city>', methods=['GET'])
def weatherinfo(city):
    schema = weatherSchema()
    weather = getWeather(city)
    high_temp = float(weather['main']['temp_max'])-273.15 # 절대온도 -> 섭씨 변환
    low_temp = float(weather['main']['temp_min'])-273.15 ## 온도 더블 체크하기
    if high_temp-low_temp > 10 : # 일교차가 클 경우(기준: 10도)
            daily = 1
            temp_data = {
                "high_temp":high_temp,
                "low_temp":low_temp,
                "daily":daily
            }
            result = schema.dump(temp_data)
    else : # 일교차가 크지 않을 경우
            daily = 0   
            temp_data = {
                "high_temp":high_temp,
                "low_temp":low_temp,
                "daily":daily
            }
            result = schema.dump(temp_data)
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
def Word2Vec_KOR(schedule):

    todo = schedule
    
    ### 테스트용 일정 ###
    todo = '회의'
    
    ### Word2Vec ###
    dataset = [['실외 액티비티'], ['실내 데이트'], ['피크닉'], ['저녁 모임'], ['비즈니스 미팅'], ['사무실'], ['가족 모임'], ['LG전자 면접'], ['회의'], ['서울숲 피크닉'], ['롯데월드'], ['소프트웨어공학 회의']]
    
    check = [''''''+todo+'''''']
    if check not in dataset:
        dataset.append(check)      
    
    model = Word2Vec(sentences = dataset, vector_size = 400, window = 10, min_count = 1, workers = 4, sg = 0)
    
    ### pre-trained language model ###
    # model = Word2Vec.load("wiki.ko.vec")
    # model = gensim.models.KeyedVectors.load_word2vec_format("wiki.ko.vec")

    try:
	    return model.wv.most_similar(todo)
    except:
	    return "없음"

    # print(model.wv.vectors.shape)
    # print(model.wv.similarity('사무실', '서울숲 피크닉'))
    # print(model.wv.most_similar(todo))
        

@app.route('/recommend/scent',methods = ['GET'])
def recommendScent():
    schedule = Word2Vec_KOR()

    ### 유사도가 가장 높은 단어 반환 ###
    # data = ['실외 액티비티', '실내 데이트', '피크닉', '저녁 모임', '비즈니스 미팅', '사무실', '가족 모임']
    # if todo in data:
    #     return todo
    # todoList = model.wv.most_similar(todo)
    # for i in range(len(todoList)):
    #     for word in data:
    #         if todoList[i][0]==word:
    #             return todoList[i][0]

    scent = Scent.query.filter(Scent.description == schedule).first()
    return jsonify(scent)