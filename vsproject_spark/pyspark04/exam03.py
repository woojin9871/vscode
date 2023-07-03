''' 
    ./data/medal.csv 파일을 읽어서
    나라별로 금메달 갯수를 파이그래프로 그리기
'''
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('./data/olympic-medals.csv')

gold = []
df_gold = df['Gold']
# print(df_gold)

for g in df_gold:
    if(g != 0):
        gold.append(g)
    
print(gold)





