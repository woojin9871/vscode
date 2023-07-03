# getter, setter
# - getter : 변수를 값을 가져오는 메소드
# - setter : 변수의 값을 지정하는 메소드

class Person:
    
    # getter
    def get_name(self):
        return self.get_name
    # setter
    def set_name(self, value):
        self.name = value
        
p = Person()

p.set('김휴먼')
print('p - name : {}'.format( p.get_name() ))