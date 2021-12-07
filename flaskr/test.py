import json
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



api_url = "https://www.googleapis.com/calendar/v3/calendars/c_gk3d37vfpjea22cdnv7f92nkdk@group.calendar.google.com/events?orderBy=startTime&singleEvents=true&timeMax="
service_key = "AIzaSyCbfMxqc1O4E2xtbUSntpsy9IwF3nTCTGA"
# API 요청시 필요한 인수값 정의
time_min = (datetime.date.today() + datetime.timedelta(days=-100)).isoformat() + "T00:00:00Z"
time_max = (datetime.date.today() + datetime.timedelta(days=100)).isoformat() + "T23:59:59Z"
url_total = api_url + time_max + "&timeMin=" + time_min + "&key=" + service_key
# API 요청하여 데이터 받기
req = requests.get(url_total)
items = req.json()
itemss = json.dumps(items, ensure_ascii=False)

print(json.loads(itemss))