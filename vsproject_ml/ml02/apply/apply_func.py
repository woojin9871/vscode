import numpy as np
import pandas as pd

# 간단한 함수 정의


def test_func(input):
    out = input*2+10
    return out


x = 5
y = test_func(x)
print(x, "==>", y)

# multi_func : 숫자를 넣으면 제곱이 되는 함수를 정의

# 50 ==> 50*50 = 2500 결과가 나오도록


def multi_func(input):
    out = input*input
    return out


result = multi_func(50)
print(result)
