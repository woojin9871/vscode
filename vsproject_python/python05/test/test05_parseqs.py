import urllib.request
import urllib.parse

URL = 'https://prod.danawa.com/info/?pcode=17033585&cate=112758'
parse = urllib.parse.urlparse(URL)
print(parse)
query = parse[4]
QS_DICT = urllib.parse.parse_qs(query)
print(QS_DICT['pcode'])
QS_DICT['pcode'] = ['11115555']
print(QS_DICT['pcode'])     # 변경이 가능

# 리스트 형식으로 반환
QS_DICT = urllib.parse.parse_qsl(query)     # 영문자 l 임
print(QS_DICT)
