'''
    csv 같은 파일이 웹상에 올라간 경우
                로컬로 다운로드 받기
                    urllib 모듈에
                                urlretrieve(소스경로, 파일경로)   파일 다운로드 함
                                src                 https://github.com/HyunchanMOON/lessons/blob/master/lessons/gasprices.csv
                                file                .data/down
                    데이터를 읽어서 출력 
'''
import urllib.request
import pandas as pd
import numpy as np

# URL = 'https://github.com/HyunchanMOON/lessons/blob/master/lessons/gasprices.csv'
# DOWN_FILE = 'C:\\kwj\\PYTHON\\vsproject_python\\data\\down\\gas.csv'

URL = 'https://raw.githubusercontent.com/developer-sdk/kaggle-python-beginner/master/datas/kaggle-titanic/train.csv'
DOWN_FILE = 'C:\\kwj\\PYTHON\\vsproject_python\\data\\down\\train.csv'

urllib.request.urlretrieve(URL, DOWN_FILE)

df = pd.read_csv(DOWN_FILE)
print(df.info())

df['Sex'] = df['Sex'].astype('category')
print(df.info())
