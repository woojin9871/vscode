# URL = "https://jsonplaceholder.typicode.com/comments"
# param   postId = 1
# request 모듈을 사용해서 get방식으로 요청결과 json() 함수를 써서 dict 값을 출력하시오

import requests

URL_JSON ='https://jsonplaceholder.typicode.com/comments'
param = { 'postId' : 1 }  
response = requests.get(URL_JSON, params=param)
if(response.status_code == 200):
    print("요청성공")
result = response.json()
print(len(result))
print(type(result[0]))