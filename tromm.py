from __future__ import print_function
from ssl import _create_default_https_context
from typing import KeysView
from flask import Flask, request, jsonify
import urllib.request
import urllib
import json
import datetime
import requests
import os.path
import csv
from http import HTTPStatus
from werkzeug.exceptions import HTTPException
from flask_sqlalchemy import SQLAlchemy
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentia
app = Flask(__name__)

# api 등 각종 key 값들 읽어오고 저장
with open('keys.csv','r',encoding='utf-8') as f:
    reader = csv.DictReader(f)
    keys = list(reader)

# 날씨 api 가져오기
def getWeather(city):
    openweather_api_url = "https://api.openweathermap.org/data/2.5/"
    service_key = keys[0]['value']

    # API 요청시 필요한 인수값 정의
    ow_api_url = openweather_api_url + "weather"
    payload = "?q=" + str(city) + "&" + "appid=" + service_key + "&lang=kr"
    url_total = ow_api_url + payload

    # API 요청하여 데이터 받기
    req = urllib.request.urlopen(url_total)
    res = req.readline()
    # 받은 값 JSON 형태로 정제하여 반환
    items = json.loads(res)
    # print(items)
    # print("============================")
    # print("도시명 : %r" % items['name'])
    # print("============================")
    # print("날씨 : %r" % items['weather'][0]['main'])
    # print("날씨상세 : %r" % items['weather'][0]['description'])
    # print("아이콘 : %r  (사이트참조: https://openweathermap.org/weather-conditions)" % items['weather'][0]['icon'])
    # print("============================")
    # print("현재온도 : %r" % str(int(items['main']['temp'])-273.15))
    # print("체감온도 : %r" % str(int(items['main']['feels_like'])-273.15))
    # print("최저온도 : %r" % str(int(items['main']['temp_min'])-273.15))
    # print("최고온도 : %r" % str(int(items['main']['temp_max'])-273.15))
    # print("습도 : %r" % items['main']['humidity'])
    # print("기압 : %r" % items['main']['pressure'])
    # print("============================")
    # print("가시거리 : %r" % items['visibility'])
    # print("풍속 : %r" % items['wind']['speed'])
    # print("풍향 : %r" % items['wind']['deg'])
    # print("============================")
    # # print("강수량 : %r (시간당)" % items['rain']['1h']) # 비 올때만 생김 caution!!
    # print("============================")
    # print("구름 : %r " % items['clouds']['all'])
    # print("일출 : %r " % items['sys']['sunrise'])
    # print("일몰 : %r " % items['sys']['sunset'])
    # print("============================")
    return items

    
# 날씨 데이터 API 활용(RestfulAPI)
@app.route('/weather/<city>',methods = ['GET'])
def weather(city):
    getWeather(city)

@app.route('/device/state/styler',methods = ['GET'])
def stateOfStyler():
    waterPercentage = 9
    if waterPercentage == 100:
        fullComment = "물이 다 찼습니다! 물을 버려주세요!"

        stylerJson = json.dumps(
        {
            'results':[
                {'waterPercentage':waterPercentage,'comment':
                    {
                    'fullComment':fullComment
                    }
                }
                    ]
        }
        ,ensure_ascii=False, indent=4)
    
    elif waterPercentage < 10:
        zeroComment = "물이 부족합니다! 물을 채워주세요!"  

        stylerJson = json.dumps(
        {
            'results':[
                {'waterPercentage':waterPercentage,'comment':
                    {
                    'zeroComment':zeroComment
                    }
                }
                    ]
        }
        ,ensure_ascii=False, indent=4)
    
    else:
        stylerJson = json.dumps(
        {
            'results':[
                {'waterPercentage':waterPercentage}
                    ]
        }
        ,ensure_ascii=False, indent=4)     
    return stylerJson


@app.route('/myCloset/add/<newClothes>',methods = ['POST'])
def getNewClothes(newClothes) :
    
    # 프론트에서(?)클라이언트에서(?) 옷 관련 정보 받아서 closet[newClothes]에 입력하기!
    closet={}
    data = request.get_json()
    closet[newClothes] = data
    # -> closet[newClothes] = {"name" : newClothes, "type" : "", "color" : "", "texture" : "", "control" : ""}

    return json.dumps(closet[newClothes])


@app.route('/device/connection',methods = ['GET'])
def connection():
    smState = True # 스마트미러 상태 불리언 값
    stState = False # 스타일러 상태 불리언 값 
    statDict = {'smState':smState,'stState':stState}
    return jsonify(statDict)


@app.route('/myHouse',methods = ['GET'])
def myHouse():
    myHumidity = 30
    myTemp = 21 
    dehum = False # 실내제습
    dry = False # 자동건조
    
    if (dehum == False) and (myHumidity >= 46):
        highHum = '지금은 실내 습도가 '+str(myHumidity)+'도로 높은 편이에요. 최적의 습도 기준인 45도로 맞추기 위해 스타일러의 실내제습을 가동시켜드릴까요?'
        if dry == False :
            dryComment = '자동건조 기능도 꺼져있으시네요! 빨래들의 빠른 건조를 위해 자동건조 기능도 같이 켜드릴까요?'        
            myHouseDict = json.dumps(
            {
            'results':[
                {
                    'condition':{
                    'Humidity':myHumidity,
                        'Temp':myTemp
                    },
                    'State':{
                        'dehumState':dehum,
                        'dryState':dry
                    },
                    'comment':{
                        'humComment':highHum,
                        'dryComment':dryComment
                    }
                }   
        ]
            }
            ,ensure_ascii=False, indent=4)
            return myHouseDict
        
        else:     
                myHouseDict = json.dumps(
                {
                'results':[
                    {
                        'condition':{
                        'Humidity':myHumidity,
                            'Temp':myTemp
                        },
                        'State':{
                            'dehumState':dehum,
                            'dryState':dry
                        },
                        'comment':{
                            'humComment':highHum,
                        }
                    }   
            ]
                }
                ,ensure_ascii=False, indent=4)
                return myHouseDict    

    else:
            myHouseDict = json.dumps(
            {
            'results':[
                {
                    'condition':{
                    'Humidity':myHumidity,
                        'Temp':myTemp
                    },
                    'State':{
                        'dehumState':dehum,
                        'dryState':dry
                    }
                }   
        ]
            }
            ,ensure_ascii=False, indent=4)
            return myHouseDict  


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
    calendar_id = keys[1]['value']
    time_min = datetime.date.today().isoformat() + 'T00:00:00+09:00'
    time_max = (datetime.date.today() + datetime.timedelta(days=10)).isoformat() + 'T23:59:59+09:00'
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
    return jsonify(events_result)        


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


### main ###
if __name__ == "__main__":
    app.run()
    