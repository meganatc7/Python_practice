from pprint import pprint
import requests

# 네이버 디벨로퍼에서 id와 secret 가져오기
naver_client_id = 'UCY4iDfEagh5LND7Upwp'
naver_client_secret = 'IYns_T1ATl'

papago_url = 'https://openapi.naver.com/v1/papago/n2mt'

source = 'ko'
target = 'en'
text = '안녕하세요.'

# 보낼 데이터
data = {
    'source': 'ko',
    'target': 'en',
    'text': '아 돈 많이 벌고 싶다.',
}

#헤더에 다음과 같은 정보를 담아서 보내야함
headers = {
    'X-Naver-Client-Id': naver_client_id,
    'X-Naver-Client-Secret': naver_client_secret,
}

# 요청 및 응답
response = requests.post(papago_url, data=data, headers=headers).json()
#pprint(response)

# 번역 결과만 가져오기
translatedText = response['message']['result']['translatedText']
print(translatedText)