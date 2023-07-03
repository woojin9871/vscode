# while 반복문을 사용하여,
# 구구단을 출력하시오

num = 1
while (num <= 9):
    goo = 1
    while (goo <= 9):
        # print (num * goo)
        print(f'{num} * {goo} : {num * goo}')
        goo += 1
    print()
    num += 1
