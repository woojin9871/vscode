text = "<title>의류쇼핑몰에 오신 것을 환영합니다</title>"
# 인덱싱을 활용
# 첫번째 글자
print(text[0])
print(len(text))    # 마지막 인덱스 = 전체 길이 -1
# 마지막 글자
print(text[len(text)-1]) 

# 반복문 0 ~ 9번째 글자 출력
for x in range(0, 10):
    print(text[x])
    
# 의류쇼핑몰 글자만 출력
result = ""
for x in range(7, 12):
    result = result + text[x]
print(result)