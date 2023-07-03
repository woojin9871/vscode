
# 파일 삭제
# os 모듈에 파일 삭제 기능이 정의되었다.

import os

path = 'C:/kwj/PYTHON/workspace/Day03/'
file = input('삭제할 파일명 : ')
file = path + file

# 파일 존재 확인
if os.path.exists(file):
    # 파일 삭제
    os.remove(file)
    print('파일이 삭제되었습니다.')
