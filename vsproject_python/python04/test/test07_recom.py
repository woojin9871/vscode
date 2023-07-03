import re

# 1번
# text = "david,010-3333-9999,test"
# m = re.search("\d{2,3}-\d{4}-\d{4}", text)
# print(m.group())

# 2번
# 패턴을 바꾸면서 사용시 편리하게
text = "david,010-3333-9999,test"
text2 = "david,010-4444-6666,test"
text3 = "david,010-2222-7777,test"
setting = re.compile("\d{2,3}-\d{4}-\d{4}")


m2 = setting.search(text2)
m3 = setting.search(text3)
print(m.group())
print(m2.group())
print(m3.group())