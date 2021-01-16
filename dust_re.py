#2
import requests           #url을 통해 요청을 보내고 응답을 받아옴
from pprint import pprint #json 형태를 좀 더 이쁘게 print출력

key = 'rYCZlgaujOdlu1V2GEYZZ3QPcMSpjF0FwlfCKgMDR2b6InRm1a9EAHdVTzTFTneiqQd27df93FX8ioBGgFGghg%3D%3D'
returnType = 'json'
numOfRows = 100
pageNo = 1
sidoName = "광주"
ver = '1.0'

url = f'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={key}&returnType={returnType}&numOfRows={numOfRows}&pageNo={pageNo}&sidoName={sidoName}&ver={ver}'

response = requests.get(url).json()
# pprint(response)

# 데이터에서 동 이름과 미세먼지 농도 가져오기
# 동 이름
stationName = ""
items = response['response']['body']['items']
for i in items:
    if i['stationName'] == '운암동':
        stationName = i['stationName']

# 미세먼지 농도
pm10Value = response['response']['body']['items'][0]['pm10Value']

# 우리 동네 미세먼지 농도 출력
print(f"현재 {stationName}의 미세먼지 농도는 {pm10Value}입니다.")

