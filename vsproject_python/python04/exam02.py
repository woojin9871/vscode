# text="게시판*hello;오라클+spring:빅데이터#취미&뉴스...."
# 패턴은 단어만 추출해서 리스트값으로 저장 후 출력

import re

text="게시판*hello;오라클+spring:빅데이터#취미&뉴스...."
L = re.findall("\w+", text)
# print(L)
for word in L:
    # print(type(word))
    print(word) 

