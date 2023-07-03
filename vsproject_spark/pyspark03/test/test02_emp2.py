from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark_ses2 = SparkSession.builder.appName('Create DataFrame').getOrCreate()

# employees.csv 파일
sdf2 = spark_ses2.read.options(header='True').csv('./data/employees.csv')

# sdf2.show()

# # employee_id, last_name, job_id, department_id 컬럼을 가져와서
sdf2.createOrReplaceTempView('sdfv_emp')
# sdf_emp2 = spark_ses2.sql('select employee_id, last_name, job_id, department_id from sdfv_emp')

# # sdf_emp2
# sdf_emp2.show()

# 부서id 20 또는 60
sdf_emp2 = spark_ses2.sql('select employee_id, last_name, job_id, department_id '+
                       'from sdfv_emp where department_id=20 or department_id = 60')
sdf_emp2.show()

# commission 컬럼을 추가 0.2값 동일하게
sdf_emp3 = sdf_emp2.withColumn('commsion', F.lit[0.2])
sdf_emp3.show()


