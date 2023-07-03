from datetime import datetime
import pandas as pd

test_df = pd.DataFrame({'order_dt': ['01-03-20', '02-03-20', '03-03-20']})
# print(test_df)

# test_df['dttm_1'] = pd.to_datetime(test_df['order_dt'], format='%d-%m-%y')
test_df['dttm_1'] = pd.to_datetime(test_df['order_dt'], format='%d-%m-%y')
#월을 글자로 출력
print(test_df)

# 오타주의 년도는 Y=4자리 y=2자리
# 01/03/20
# %d/%m/%y 년도 2020
# %y/%m/%d 년도 2001
# %m/%y/%d 년도 2003

# 01-03-20 
# %d-%m-%y 월 
# print(test_df['dttm_1'].dt.strftime('%Y-%b-%d'))

today = datetime.now()
today2 = today.strftime('%Y-%b-%d')
# print(today2)

time = today.strftime('%H:%M:%S')
# print(time)

test_df['dttm_1']   # 시리즈 데이터프레임 => 보통 반복문이 필요하다
print(test_df['dttm_1'].dt)
for dttm in test_df['dttm_1']:
    print(dttm.strftime('%Y-%b-%m'))
    