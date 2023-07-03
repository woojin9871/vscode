# 파이썬 2 까지는 import urllib
# 파이썬 3 부터
import urllib.request

URL = "https://www.naver.com"
req = urllib.request.Request(URL)
# print(req)

# 주소를 열어=통신함
response1 = urllib.request.urlopen(URL)
# print(response1)

byte_data = response1.read(1000)
text_data = byte_data.decode()

# response2 = urllib.request.urlopen(req)
# print(response2)