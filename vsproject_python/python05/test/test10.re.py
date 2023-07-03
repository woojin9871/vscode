import urllib.request
import re

# URL="https://search.naver.com/search.naver?query=python"
URL="https://search.naver.com/search.naver?query="

query = 'python'    #검색어
keyword = '파이썬'
keyword2 = '직군별'
keyword3 = '개발자'
NEWURL = URL + query
req = urllib.request.Request(NEWURL)
response = urllib.request.urlopen(req)
byte_data = response.read()
# print(byte_data.decode())  # 보안으로 막히지 않음
text_data = byte_data.decode()  # text html 문자열
# test
# print(text_data.find('파이썬'))
result_keyword = text_data.split(keyword)[1]    # 큰덩어리 1개 발견
# print(result_keyword.find('직군별'))
result_keyword2 = result_keyword.split(keyword2)[0]     # 중간덩어리 1개 발견
# print(result_keyword2.find('개발자'))
result_keyword3 = result_keyword2.split(keyword3)[1]    # 작은덩어리 1개 발견
# print(result_keyword3) # 일부분의 html 태그


#정규식
result_final = re.sub('<.+?>', '', result_keyword3)
result_final = result_final.replace("   ", " ").strip()
print(result_final)

f = open('sample.txt', 'w', encoding="UTF-8")    #한글 깨짐 방지
f.write(result_final)
f.close()