# 1

from flask import Flask # flask라는 패키지에서 Flask모듈을 import하여 
                        # 플라스크를 사용할 수 있도록 설정

# __name__변수는 파이썬이 내부적으로 사용하는 특별한 변수명
# __name__이 __main__이라는 값을 가지게 되면 해당 모듈이 주 프로그램이라는 소리이고, 해당 모듈을
# 실행시키지 않고 import 했을 때는 모듈 이름이 __name__으로 들어가게 된다.
# 그렇게 app 이라는 변수로 Flask모듈을 쓸 수 있도록 한 것?
app = Flask(__name__)

# @app.route는 예로 naver.com/reddit 이라는 주소가 있다면,
# naver.com은 도메인을 뜻해서 불변이고 reddit이라는 주소 부분이 @app.rout()에 들어가는 부분이다.
# 즉, 예시처럼 라우팅 하려면 @app.rout('/reddit')으로 작성하면 되는 것이다.
# 라우팅을 한 다음에는 그 라우팅하는 주소에 대한 함수를 선언하는데(이건 플라스크의 일종의 규칙)
# 함수 선언을 통해 해당 주소에서 어떻게 작동할 지를 선언해 주는 것이다.
# Hello World!를 리턴해서 문구가 뜨도록 한다.
@app.route('/')             # /앞에 http://127.0.0.1:5000이 생략된 것
def hello_world():
    return 'Hello World!'

# __name__에 __main__이 들어있는지 확인해 주는 소스
# 즉 flask서버를 실행시킬 때 app.py가 실행되니까 __name__에는 __main__이 들어가서 app.run()이 실행
if __name__ == '__main__':
    app.run()