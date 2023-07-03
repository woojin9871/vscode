# Spark SQL 가져오려면
from pyspark.sql import SparkSession    # 클래스

spark_ses = SparkSession.Builder().appName("PySpark DataFrame").getOrCreate()

df = spark_ses.read.options(header='True').csv('./data/test_save.csv')

df.show()