bank = 0            # 저금통
money = 10000       # 가진 돈

# 복합 대입 연산자
bank += money       # bank = bank + money
print('통장에 돈을 {}원 입급하였습니다.'.format(money))
print('통장에는 {} 원이 있습니다'. format(bank))

snack = 2000

bank -= snack       # banl = bank - snack
print('{}원 짜리과자를 구입하였습니다.'.format(snack))
print('통장에는 {} 원이 있습니다.'.format(bank))