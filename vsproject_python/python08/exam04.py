'''
    movie-ratings.csv 파일을 읽어온다
        100번째     모든 컬럼값
        200번째     장르만
        맨 마지막에 행 데이터 추가
                    back to the future      action      80,70,40    2000
        300번째     영화 제목 출력후 삭제
        400번쨰     rating값에 -5 하여 수정
'''
import pandas as pd

df = pd.read_csv('./data/movie-ratings.csv')

print(df)