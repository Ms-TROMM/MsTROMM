# 🖥️ Ms.TROMM
### Wise Secretary Always Thinking about You: 
### Artificial Intelligence-based Recommendation Software using Styler and Smart Mirror
----------
## 🔥 Contributors
##### JIN HO KIM, Department of Information System
##### GA HEE HAN, Chinese Language and Literature
##### YU JIN HER, Department of Information System
##### EO JIN LEE, Department of Information System
----------
## ✨ Details
https://dot-nasturtium-ee3.notion.site/Ms-TROMM-e65d5d40ac7044b797a5c9955d5e4b8d


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

- 프로젝트 폴더 밑에 `.env` 파일 만들어서 환경변수 설정. `settings.py` 파일에서도 아래의 환경변수에서 DB 주소를 읽어온다. 

```
# .env 파일 내부에 작성 

DEBUG=True
FLASK_ENV=development
FLASK_APP=wsgi

CLEARDB_DATABASE_URL=mysql://{USERNAME}:{PASSWORD}@{HOST}/{DATABASE NAME}
# database uri should not be exposed to public, contact the team for exact uri. 
```


- 새로운 패키지를 개발 도중에 받은 경우 pip freeze 를 다시 실행해준다.

```shell 

pip3 freeze > requirements.txt 

```

### Heroku 

- main 브랜치에 푸시하면 바로 API 가 배포될 수 있는 옵션 존재. 지금은 꺼져있는 상태임. 


