st_name = ['송지우', '심현준', '윤호민']
st_score = [90, 78, 89]

for n in st_name:
    print('이름 : ' + n)

for s in st_score:
    print('점수 : ' + str(s))

for c in st_score:
    if (c >= 90):
        print('학점 : A')
    elif (c >= 80):
        print('학점 : B')
    elif (c >= 70):
        print('학점 : C')
    elif (c >= 60):
        print('학점 : D')
    else:
        print('학점 : F')
    
        
