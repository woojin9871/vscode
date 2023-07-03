# requests 요청
import requests

# URL = "https://www.naver.com"
# response = requests.get(URL)
# print(response.status_code)
# print(response.text)

# https://search.naver.com/search.naver?query=bigdata

URL = "https://search.naver.com/search.naver"
param = { 'query' : 'bigdata'}
response = requests.get(URL, params=param)
print(response.status_code)
print(response.text)