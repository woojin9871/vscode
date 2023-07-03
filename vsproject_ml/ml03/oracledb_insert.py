import oracledb
import pandas as pd

conn = oracledb.connect(user='jsp5', password='123456',
                        dsn='192.168.0.156:1521/orcl')

cursor = conn.cursor()

sql = 'INSERT INTO test (ID, NAME, CLASS_ID) VALUES (NVL(MAX(ID), 0)+100 FROM test) ,:1, :2)'
cursor.execute(sql, ('양정호', 10 ))

print(cursor.rowcount)

cursor.close()
conn.commit()
conn.close()