import re

text = "1111<head>안녕하세요</head>2222"
# <head>안녕하세요</head>
# re.search(정규식, 검색할 문자열)
m = re.search("<head.*/head>", text)    # match 객체 None 또는 값
print(m.group())

print()

text = "###event result###"
# event result
m = re.search("[a-z]*\s[a-z]*", text)
print(m.group())

print()

text = "david,010-3333-9999,test"
# 010-3333-9999 를 추출하여 출력
m = re.search("\d{2,3}-\d{4}-\d{4}", text)
print(m.group())
