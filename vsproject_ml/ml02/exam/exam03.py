'''
    y축(특성2)
        10                   --------------------
        9                   ㅣ          B(8,9)  ㅣ
        8           X(4,8)  ㅣ                  ㅣ      
        7                   ㅣ                  ㅣ
        6                   ㅣ                  ㅣ
        5 ------------------ㅣ-------------------
        4                   ㅣ
        3   A(2,3)          ㅣ
        2                   ㅣ
        1                   ㅣ
            1   2   3   4   5   6   7   8   9   10  
                                                    x축(특성1)
'''
import numpy as np
import pandas as pd
import math

a = np.array((2, 3))
b = np.array((8, 9))
x = np.array((4, 8))

dist_a = np.linalg.norm(a - x)
dist_b = np.linalg.norm(b - x)

print(dist_a)
print(dist_b)

if(dist_a < dist_b):
    print('a점과 가깝다')
elif(dist_a > dist_b):
    print('b점과 가까움')
else:
    print('동일함')
    
# A점 (x, y)
a = [2, 3]  # 0번째 -2, 1번째 -3
b = [8, 9]
x = [4, 8]

# 두 점의 거리공식을 사용하는 점이 많다면 함수로 정의하면 효율적
def distance(Lst1, Lst2):
    rst = math.sqrt(math.pow((Lst1[0] - Lst2[0]), 2) +
                    math.pow((Lst1[1] - Lst2[1]), 2))
    return rst

# pow(x, 2) - x*x
# math.sqrt(x) = x의 제곱근
ax = math.sqrt(math.pow((a[0] -x[0]), 2) + math.pow((a[1] -x[1]), 2))
bx = math.sqrt(math.pow((b[0] -x[0]), 2) + math.pow((b[1] -x[1]), 2))
print(ax)
print(bx)

if(ax < bx):
    print('a점과 가깝다')
elif(ax > bx):
    print('b점과 가까움')
else:
    print('동일함')