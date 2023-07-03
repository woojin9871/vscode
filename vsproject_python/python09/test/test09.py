import pandas as pd
import numpy as np
import glob as  glob

files = glob.glob('./data/small_biz/*.csv')
# print(type(files))v

df_tot = pd.DataFrame()

for file in files:
    df_temp = pd.read_csv(file, low_memory=False)
    # print('각각의 파일데이터 행 갯수 : ', df_temp.shape[0])
    df_tot = pd.concat([df_tot, df_temp])
    # df_tot = df_tot.append(df_temp)   # deprecated
    
print('전국 총 상점 갯수 : ', df_tot.shape[0])    
    