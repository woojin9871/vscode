'''
    CSV (Comma Separared Value)
    : 콤마(,) 분리한 값들
    
    ex)
        학번, 이름, 주소, 전화번호
        101, 김휴먼, 서울시 영등포구, 010-1111-2222
        102, 김휴먼, 서울시 영등포구, 010-1111-2222
        103, 김휴먼, 서울시 영등포구, 010-1111-2222
        104, 김휴먼, 서울시 영등포구, 010-1111-2222
'''

import csv

path = 'C:/kwj/PYTHON/workspace/Day03/'
file = path + 'test.csv'

#open(파일경로, 모드, 옵션)
with open(file, 'w', newline='', encoding='UTF-8') as file:
    # delimiper : 구분기호
    # writer(파일객체, delimiter="구분기호")
    # : 파일을 작성하는 기능을 가진 writer 객체를 반환
    csv_maker = csv.writer(file, delimiter=',')
    
    # writer 객체가 가진 기능 : writerow()
    # : 파일객체에 한 줄씩 데이터를 작성하는 함수
    csv_maker.writerow(['학번', '이름', '주소', '전화번호'])
    csv_maker.writerow(['101', '김휴먼', '서울시 영등포구', '010-1111-2222'])
    csv_maker.writerow(['102', '김휴먼', '서울시 영등포구', '010-1111-2222'])
    csv_maker.writerow(['103', '김휴먼', '서울시 영등포구', '010-1111-2222'])
    csv_maker.writerow(['104', '김휴먼', '서울시 영등포구', '010-1111-2222'])
    
print('파일이 생성되었습니다.')