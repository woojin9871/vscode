# params 복수의dict() 만들어서
# request 모듈을 사용하서 get방식으로 요청결과 text를 출력하시오

import requests

URL = "https://www.ajou.ac.kr/kr/ajou/notice.do"
params = { 'mode':'view', 'articleNo':210213, 'article.offset':0 ,'articleLimit':10 }    
#?mode=view&articleNo=210213&article.offset=0&articleLimit=10
response = requests.get(URL, params=params)
if(response.status_code == 200): 
    print('요청성공')
    print(response.text)