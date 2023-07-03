import requests

URL = "https://www.google.com/search"
param = { 'q' : 'machine'}
response = requests.get(URL, params=param)
if(response.status_code==200):
    # print("요청성공")
    print("응답결과:")
    print(response.text)