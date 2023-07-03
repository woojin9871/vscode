import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 인구 비율 서울, 경기, 부산, 광주 
ratio = [42, 38, 12, 8]
print(type(ratio))
cities = ['Seoul', 'Gyunggi', 'Busan', 'Kyungju']
print(ratio)
plt.pie(ratio, labels=cities, autopct='%.1f%%', startangle=90, counterclock=False)
plt.show()