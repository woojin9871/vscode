text = "    <title>의류쇼핑몰의 메인에 오신 것을 환영합니다</title>    "
# 4개의 좌우에 공백이 있음
print(";;" + text.strip() + ";;")

# 오른쪽 공백만 제거
print(";;" + text.rstrip() + ";;")

# 왼쪽 공백만 제거
print(";;" + text.lstrip() + ";;")