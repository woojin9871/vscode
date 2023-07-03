'''
    영어 점수 = 75
    90점 이상 학점 A
        90 ~ 94 A 아니면 95이상 A+
    80점 이상 학점 B
        80 ~ 84 B 아니면 85이상 B+
    70점 이상 학점 C
        90 ~ 94 C 아니면 95이상 C+
    60점 이상 학점 D
        60 ~ 64 D 아니면 95이상 Ds+
    나머지 F
'''

english = input('점수를 입력하세요 : ')
english = int(english)

if (english >= 90):
    if (90 >= english <= 94 ):
        print('학점은 A')
    elif (english >= 95):
        print('학점은 A+')
elif (english >= 80):
    if (80 >= english <= 84 ):
        print('학점은 B')
    elif (english >= 85):
        print('학점은 B+')
elif (english >= 70):
    if (70 >= english <= 74 ):
        print('학점은 C')
    elif (english >= 75):
        print('학점은 C+')
elif (english >= 60):
    if (60 >= english <= 64 ):
        print('학점은 D')
    elif (english >= 65):
        print('학점은 D+')
else:
    print('학점은 F')
    
    
