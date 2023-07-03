import pandas as pd
import numpy as np

data = {
    'weather' : ['sunny', 'sunny', 'overcast', 'rainy', 'rainy'],
    'temp' : ['hot', 'hot', 'hot', 'mild', 'cool'],
    'humidity' : ['high', 'high', 'high', 'high', 'normal'],
    'windy' : ['FALSE', 'TRUE', 'FALSE', 'FALSE', 'FALSE'],
    'basket_target' : ['no', 'no', 'yes', 'yes', 'yes']
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
arr_basket = df_basket.to_numpy
print(arr_basket)