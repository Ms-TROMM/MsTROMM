# 🖥️ Ms.TROMM
### Wise Secretary Always Thinking about You: 
### Artificial Intelligence-based Recommendation Software using Stylers and Smart Mirror
----------
## 🔥 Contributors
##### JIN HO KIM, Department of Information System
##### GA HEE HAN, Chinese Language and Literature
##### YU JIN HER, Department of Information System
##### EO JIN LEE, Department of Information System
----------
## ✨ Details
https://dot-nasturtium-ee3.notion.site/Ms-TROMM-60cbd1c9759f438e8e7ede45385a6d1b


---

- https://flask.palletsprojects.com/en/2.0.x/tutorial/layout/ 와 같은 폴더 구조를 따른다. 

#### How to start 

> Python 3을 사용한다. 

```shell 

python3 --version # python3 있는지 확인 

pip3 install --user virtualenv # virtualenv 다운로드 

python3 -m venv env # 가상환경 생성 

# 가상환경 시작하기 
source env/bin/activate # Mac
.\env\Scripts\activate # Windows 

# 가상환경 안에서 패키지 다운받기 
pip3 install -r requirements.txt

```


- https://flask.palletsprojects.com/en/2.0.x/tutorial/factory/#run-the-application 에 나와있는대로 환경변수 설정 

```shell 
# Mac 

$ export FLASK_APP=flaskr
$ export FLASK_ENV=development
$ flask run

# Windows 

$env:FLASK_APP = "flaskr"
$env:FLASK_ENV = "development"
flask run
```

- 새로운 패키지를 개발 도중에 받은 경우 pip freeze 를 다시 실행해준다.

```shell 

pip3 freeze > requirements.txt 

```

---

### Heroku 

- Created cleardb-fitted-66992 as CLEARDB_DATABASE_URL


