# URL = "https://jsonplaceholder.typicode.com/comments"
# request 모듈을 사용해서 get 방식으로
# 요청결과 json() 함수를 써서 dict값을 출력하시오

import requests

URL_JSON ='https://jsonplaceholder.typicode.com/comments'
response = requests.get(URL_JSON)
if(response.status_code == 200):
     print(response.json())


URL_JSON ='https://jsonplaceholder.typicode.com/comments'
result = list()
response = requests.get(URL_JSON)
if(response.status_code == 200):
    print('요청성공')
    result = list(response.json())
print(result[0])