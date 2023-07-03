sample_data = '''
<div id='test'>
<div id="darkmodemenu" 
    class="ws-black test" 
    onmouseover="mouseoverdarkicon()" 
    onmouseout="mouseoutofdarkicon()">
    <h2>테스트코드</h2>
</div>
</div>
'''
#아이디는 값이 1개 뿐
#클래스는 값이 1개 이상

from bs4 import BeautifulSoup
soup = BeautifulSoup(sample_data, 'html.parser')
# print(soup.prettify()) # 파싱 확인 
# h2 전체를 출력
print(soup.h2.string)
# div의 클래스속성 출력
# print(soup.div['class'])
# print(soup.div('class="test"'))
# div의 onmouseout속성 출력
# sub_html = soup.div['onmouseout']
sub_html=soup.find('div', id='darkmodemenu')


# soup2 = BeautifulSoup(sub_html, 'html.parser')
# print(soup2.prettify()) # 파싱 확인 
# 아이디는?
# print(soup.div['id'])