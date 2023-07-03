'''
        weather     tmep        humidity    windy   basket_target 
    0   sunny       hot         high        FALSE   no
    1   sunny       cool        normal      FALSE   yes
    2   sunny       mild        high        TRUE    yes
    3   overcast    hot         high        FALSE   yes
    4   rainy       mild        high        FALSE   no
    5   rainy       cool        normal      FALSE   no
    6   sunny       hot         normal      FALSE   no
    7   sunny       mild        normal      FALSE   yes
    8   rainy       mild        high        TRUE    yes
    9   overcast    cool        high        FALSE   yes
        0, 1, 2     30, 20, 10  50, 40      1, 0    0, 1
'''
import pandas as pd
import numpy as np

data = {
    'weather' : ['sunny', 'sunny', 'sunny', 'overcast', 'rainy', 'rainy', 'sunny', 'sunny', 'rainy', 'overcast'],
    'temp' : ['hot', 'coll', 'mild', 'hot', 'mild', 'cool', 'hot', 'mild', 'mild', 'cool'],
    'humidity' : ['high','normal', 'high', 'high', 'high', 'normal', 'normal', 'normal', 'high', 'high'],
    'windy' : ['FALSE', 'FALSE', 'TRUE', 'FALSE', 'FALSE', 'FALSE', 'FALSE', 'FALSE', 'TRUE', 'FALSE'],
    'basket_target' : ['no', 'yes', 'yes', 'yes', 'yes', 'no', 'no', 'yes', 'yes', 'yes']
}

df_basket = pd.DataFrame(data)
# print(df_basket)

df_basket['weather'] = df_basket['weather'].replace(['sunny', 'overcast', 'rainy'], [0, 1, 2])

df_basket['temp'] = df_basket['temp'].replace(['hot', 'mild', 'cool'], [30, 20, 10])

df_basket['humidity'] = df_basket['humidity'].replace(['high', 'normal'], [50, 40])

df_basket['windy'] = df_basket['windy'].replace(['FALSE', 'TRUE'], [1, 0])

df_basket['basket_target'] = df_basket['basket_target'].replace(['no', 'yes'], [0,1])
print(df_basket)

# df_basket => numpy
# arr_basket = df_basket.to_numpy
# print(arr_basket)