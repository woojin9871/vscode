'''
    192.168.0.156 디비  
    개인 pc (집에 계시면)
    테스트 계정 사용 userid, userpw
    test 테이블
'''
import oracledb
import pandas as pd

conn = oracledb.connect(user='jsp5', password='123456',
                     dsn='192.168.0.156:1521/orcl')
# print(conn)

curs = conn.cursor()

# sql = "SELECT COUNT(*) AS CNT FROM test"
dql = "SELECT "
curs.execute(sql)

# out_data = curs.fetchone()
out_data = curs.fetchall()

# print(out_data) # 몇개인지 체크
# for t in out_data:
#     print(t)

df = pd.Data