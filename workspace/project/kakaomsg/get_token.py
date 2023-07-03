'''
    1. 인가코드 받기
    https://kauth.kakao.com/oauth/authorize?client_id=${REST_API_KEY}&redirect_uri=${REDIRECT_URI}&response_type=code

    - ${REST_API_KEY} : 내 어플리케이션 > REST API 키
    - ${REDIRECT_URI} : https://localhost.com
    
    # 인가 코드 요청 경로
    https://kauth.kakao.com/oauth/authorize?client_id=a618a871855acabca43b5ce2270a3af9&redirect_uri=https://localhost.com&response_type=code
'''

'''
    2. 인증 토큰 받기
'''
import requests

url = 'https://kauth.kakao.com/oauth/token'

data = {
    'grant_type'    :   'authorization_code',
    'client_id'     :   'a618a871855acabca43b5ce2270a3af9',      # REST API 키
    'redirect_uri'  :   'https://localhost.com',                 #
    'code'          :   'lIDIdvyQgZoYlT4a0cYQmtjHFjOj4GuycYsQ8R3LM2GTaTAoDnMxO-Nyw7SSRf0Mf6zu8QopyNkAAAGF8JdP6w'    # 인가 코드
}

response = requests.post(url, data=data)

# 요청 실패 시
if response.status_code != 200:
    print('오류가 발생하였습니다.', response.json())
else:
    token = response.json()
    print(token)