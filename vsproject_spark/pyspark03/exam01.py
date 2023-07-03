'''
    ./data/zipdoro.csv
    우편번호 코드를 pyspark를 가지고 읽어서 출력하시오
'''
from pyspark.sql import SparkSession

spark_ses = SparkSession.Builder().appName("PySpark DataFrame").getOrCreate()

df = spark_ses.read.csv('./data/zipdoro.csv')
df = df.withColumnRenamed('_c0', 'code')
df = df.withColumnRenamed('_c1', 'address')

df.show()
