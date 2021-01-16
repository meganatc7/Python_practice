from pprint import pprint
import requests
import random

# telegram 봇 만들고 토큰 받아오기
token = '1513904019:AAHHNNr6GjznPfDR4SdI-qFeT-nvktROHug'

#getMe method는 봇에 대한 기본 정보
#url = f'https://api.telegram.org/bot{token}/getMe'

# getUpdates method는 봇이 받은 메시지 정보를 담고있음
# 해당 메소드로 정보를 본 다음 메시지 전송인의 id를 chat_id에 담는다.
url = f'https://api.telegram.org/bot{token}/getUpdates'
response = requests.get(url).json()
#pprint(response)
chat_id = response['result'][0]['message']['chat']['id']
#print(chat_id)

# sendMessage method로 chat_id에 담긴 전송인에게 일방적으로 메시지 보내기
text = "Nice to meet you, bro"
message_url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
#response = requests.get(message_url)

# 로또 번호 6개 보내기
lotto = range(1,46)
lotto_num = sorted(random.sample(lotto,6))
lotto_num = ', '.join(map(str, lotto_num)) #리스트의 대괄호 없애는 소스
text = f'이번 주 로또 당첨 번호는 {lotto_num}입니다.'
message_url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
response = requests.get(message_url)

#===========================================================
#미세먼지 정보 보내기
#dust_re.py에서 코드 가져와 사용
key = 'rYCZlgaujOdlu1V2GEYZZ3QPcMSpjF0FwlfCKgMDR2b6InRm1a9EAHdVTzTFTneiqQd27df93FX8ioBGgFGghg%3D%3D'
returnType = 'json'
numOfRows = 100
pageNo = 1
sidoName = "광주"
ver = '1.0'

url = f'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={key}&returnType={returnType}&numOfRows={numOfRows}&pageNo={pageNo}&sidoName={sidoName}&ver={ver}'

response = requests.get(url).json()

stationName = ""
items = response['response']['body']['items']
for i in items:
    if i['stationName'] == '운암동':
        stationName = i['stationName']

pm10Value = response['response']['body']['items'][0]['pm10Value']

# 우리 동네 미세먼지 농도 메시지 전송~!
text = f"현재 {stationName}의 미세먼지 농도는 {pm10Value}입니다."
message_url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
requests.get(message_url)
#=========================================================================