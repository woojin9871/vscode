import urllib.request
import urllib.parse

URL ='https://www.nate.com/?f=auto_news'
# 도메인명을 www.naver.com 로 변경
Temp = urllib.parse.urlparse(URL)
LTemp = list(Temp)
# Temp[1]='www.naver.com'
LTemp[1]='www.naver.com'

result = urllib.parse.urlunparse(LTemp)
print(result)