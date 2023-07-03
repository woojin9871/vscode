import requests

URL="http://homepage.bluevation.co.kr/"
response = requests.get(URL)
if(response.status_code==200):
    print('요청성공')
else: 
    print('요청실패')