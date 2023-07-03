text = "<title>의류쇼핑몰의 메인에 오신 것을 환영합니다</title>"
print(text.find('의'))      # 7 처음것만 찾음
print(text.find('손'))      # -1 없다
print(text.find('메인'))    # 14

print()

print(text.index('의'))
print(text.index('메인'))   # 14
print(text.index('손'))     # 에러가 나면 프로그램 종료

