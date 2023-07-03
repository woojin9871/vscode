text = "    <title>의류쇼핑몰의 메인에 오신 것을 환영합니다</title>    "
text2 = text.strip()
print(text2)

# title => div
print(text2.replace("title", "div"))

# <title> 제거
print(text2.replace("<title>", "")
           .replace("</title>", ""))

# 정규식을 이용한 방법