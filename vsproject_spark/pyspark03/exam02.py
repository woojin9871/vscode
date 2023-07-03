'''
    PySpark 에 SparkSession을 사용하여 departments.csv 를 읽어온다
    LOCATION_ID 가 1700인 부서의 목록을 모두 출력하시오
'''
from pyspark.sql import SparkSession

spark_s = SparkSession.builder.appName('create DF').getOrCreate()

sdf = spark_s.read.options(header='True').csv('./data/departments.csv')

# sdf.show()

sdf.createOrReplaceTempView('sdfv_emp')

sdf_emp = spark_s.sql('select department_name, location_id' +
                      ' from sdfv_emp where location_id = 1700')   
sdf_emp.show()