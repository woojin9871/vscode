# 인스턴스 변수, 메소드
# 클래스 변수, 메소드
'''
    class 클래스명:
        # 클래스 변수
        클래스변수명 = 값

        # 클래스 메소드
        @classmathod
        def 메소드명(cls):
            메소드 내용
            
        # cls : 클래스
        
    클래스 변수에 접근
    - 클래스명.변수명        
'''

class Student:
    # name = ''    # 기본값 초기화
    # age = 0  
    # tel = ''
    # 클래스 변수 - 객체간에 공유할 값을 사용하는 변수
    count = 0

    def __init__(self, name, age, tel):
        # 인스턴스 변수 - 객체 별로 다르게 사용할 변수
        self.name = name
        self.age = age
        self.tel = tel
        Student.count += 1
        Student.student_list.append(self)
    
    def __str__(self):
        return '{} / {} / {}'.format(self.name, self.age, self.tel)
    
    # 클래스 메소드
    # @이름 : 데코레이터, 해당 클래스나 메소드의 기능/용도를 명시하는 역할
    # @classmethod : 해당 메소드를 클래스 메소드로 명시
    @classmethod
    def show_info(cls):
        for student in cls.student_list:
            print( str(student) )
       
s1 = Student("김휴먼", 20, '010-1111-2222')
s2 = Student("이효리", 20, '010-1111-2222')
s3 = Student("손석구", 20, '010-1111-2222')

print('{} 명의 학생이 참여하였습니다.'.format( Student.count ))

print( Student.show_info() )