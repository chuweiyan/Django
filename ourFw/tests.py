import requests
import json

# res = requests.post('http://127.0.0.1:8000/polls/population/', data=json.dumps({'from': 150, 'to': 250}))
# print('222')
# print(res)

res = requests.post('http://127.0.0.1:8000/ourFw/terminalG4CountCity/', data=json.dumps({'from': 150, 'to': 250}))
# print('222')
print(res)
