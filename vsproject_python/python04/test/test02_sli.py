text = "<title>의류쇼핑몰에 오신 것을 환영합니다</title>"
# 제목 글자만 추출
subject = text[7:25]
print(subject)

# 하나 건너뛰어서 글자 출력
# 의쇼몰 신것...
subject = text[7:25:2]
print(subject)