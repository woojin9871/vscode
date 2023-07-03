import pandas as pd

Aclass = pd.Series([70, 60, 55, 75, 95, 90, 80, 80, 85, 100])

print('총 학생 수 : ' + str(Aclass.size))

print('합계 : ' + str(Aclass.sum()))

print('평균 : ' + str(Aclass.mean()))
