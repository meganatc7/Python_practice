import requests
from pprint import pprint

# 텔레그렘 봇 토큰
token = '1513904019:AAHHNNr6GjznPfDR4SdI-qFeT-nvktROHug'

# 텔레그렘 봇 url
url = f'https://api.telegram.org/bot{token}/getUpdates'

# getUpdates 메소드로 요청을 보내서 가장 최근의 메시지를 messgae 변수에 담기
response = requests.get(url).json()
for i in range(len(response['result'])):
    if i == int(len(response['result']))-1:
        message = response['result'][i]['message']['text']
print(message)
