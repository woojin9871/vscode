# 데코레이터를 이용한 gettet, setter 정의

class Person:
    
    # @property : 해당 변수를 데코레이터 기능을 사용할 수 있도록 지정
    #            - 필드의 역할을 기능인 ssetter, getter 로 사용가능
    #            - @property 로 지정한 변수는 __변수와 같은 형태로 사용
    @property
    def name(self):
       return self.__name
    
    # @변수.setter : 해당 메소드를 setter 메소드가 실행
    #                - (객체.변수 = 값) 문장실행 시, --> 지정한 setter 메소드가 실행
    @name.setter
    def name(self, value):
        self.__name = value
        print('setter 메소드 호출...')

    # @변수.getter : 해당 메소드를 setter 메소드가 실행
    #                - (객체.변수) 문장실행 시, --> 지정한 getter 메소드가 실행
    @name.getter
    def name(self):
        print('getter 메소드 호출...')
        return self.__name
    
p = Person()

p.name = '김휴먼'
print('p - name : {}'.format( p.name ))