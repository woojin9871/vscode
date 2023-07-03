import re

# text = "1 orange#, 2 apple;, 3 banana 4 mango|"
# L = re.findall("\d\s\w+", text)
# print(type(L))
# for x in L:
#     print(x)


text="사과:apple#자동차:car&&호랑이:tiger**친구:friend"
# 패턴 - 문자:문자 - findall
L = re.findall("[가-힣]+:[a-z]+", text)
# L = re.findall('[\w:\w]+', text)
for word in L:
    # print(type(word))
    temp = word.split(':')  #사과:apple
    print(temp)
