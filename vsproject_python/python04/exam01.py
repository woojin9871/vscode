import re

text = "###s13579"
text2 = "###w13579"
# 패턴 : 문자 + 숫자 5개
# 찾아서 출력하기

setting = re.compile("\w.*\w")
m = setting.search(text)
m2 = setting.search(text2)
print(m.group())
print(m2.group())

text3 = "##s13579##4abcd##ss123"
setting2 = re.compile("\w")

m3 = setting2.search(text3)

print(m3.group())