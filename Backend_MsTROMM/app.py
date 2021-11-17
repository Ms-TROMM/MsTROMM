from flask import Flask, request, jsonify
import urllib.request
import urllib
import json

app = Flask(__name__)
 
@app.route('/userLogin', methods = ['POST'])
def userLogin():
    user = request.get_json()   # json 데이터를 받아옴
    return jsonify(user)    # 받아온 데이터를 다시 전송
 
@app.route('/environments/<language>')
def environments(language):
    return jsonify({"language":language})


# 날씨 데이터 API 활용(RestfulAPI)
@app.route('/weather/<city>',methods = ['POST'])
def getNowCity(city) :
    openweather_api_url = "https://api.openweathermap.org/data/2.5/"
    service_key = "TOKEN"

    # API 요청시 필요한 인수값 정의
    ow_api_url = openweather_api_url + "weather"
    payload = "?q=" + str(city) + "&" + "appid=" + service_key + "&lang=kr" # 옵션을 추가하면 날씨설명을 한글로 받을 수 있음
    url_total = ow_api_url + payload

    # API 요청하여 데이터 받기
    req = urllib.request.urlopen(url_total)
    res = req.readline()

    # 받은 값 JSON 형태로 정제하여 반환
    items = json.loads(res)
    print(items)
    print("============================")
    print("도시명 : %r" % items['name'])
    print("============================")
    print("날씨 : %r" % items['weather'][0]['main'])
    print("날씨상세 : %r" % items['weather'][0]['description'])
    print("아이콘 : %r  (사이트참조: https://openweathermap.org/weather-conditions)" % items['weather'][0]['icon'])
    print("============================")
    print("현재온도 : %r" % str(int(items['main']['temp'])-273.15))
    print("체감온도 : %r" % str(int(items['main']['feels_like'])-273.15))
    print("최저온도 : %r" % str(int(items['main']['temp_min'])-273.15))
    print("최고온도 : %r" % str(int(items['main']['temp_max'])-273.15))
    print("습도 : %r" % items['main']['humidity'])
    print("기압 : %r" % items['main']['pressure'])
    print("============================")
    print("가시거리 : %r" % items['visibility'])
    print("풍속 : %r" % items['wind']['speed'])
    print("풍향 : %r" % items['wind']['deg'])
    print("============================")
    # print("강수량 : %r (시간당)" % items['rain']['1h']) # 비 올때만 생김 caution!!
    print("============================")
    print("구름 : %r " % items['clouds']['all'])
    print("일출 : %r " % items['sys']['sunrise'])
    print("일몰 : %r " % items['sys']['sunset'])
    print("============================")
    return items


if __name__ == "__main__":
    app.run()