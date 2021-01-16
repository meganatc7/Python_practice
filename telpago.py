import requests
from pprint import pprint

token = '1513904019:AAHHNNr6GjznPfDR4SdI-qFeT-nvktROHug'

url = f'https://api.telegram.org/bot{token}/getUpdates'
response = requests.get(url).json()
#pprint(response)
#message = response['result'][1]['message']['text']
for i in range(len(response['result'])):
    if i == int(len(response['result']))-1:
        message = response['result'][i]['message']['text']
print(message)
