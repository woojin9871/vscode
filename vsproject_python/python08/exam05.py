'''
    2016_sleep_driver.csv 파일을 읽어온다

        7월에 있는 교통사고 건수, 부상수를 출력하시오
        부상자 컬럼의 총합을 구하시오
'''
import pandas as pd

df = pd.read_csv('./data/2016_sleep_driver_accident.csv')

print(df.loc[:6,'사고(건)'])
print(df.sum[])