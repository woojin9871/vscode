import random # 표준모듈

# 1 2 3 4 5 6
# 5 4 5 6 7 3
# 로또, 주사위, 윷놀이
# N = 6
# for x in range(1,11):
#     print(int(random.random() * N)+1)
# 결과 < 1 && 결과 >= 0


# 카드 셔플
card = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(card)
random.shuffle(card)
print(card)
