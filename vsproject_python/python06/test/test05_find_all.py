from bs4 import BeautifulSoup

sample_data = '''
    <a href="https://www.w3schools.com" class="w3-nav-item" title="Home" style="width:77px">
        <i id="demo" style="position:relative;font-size:42px!important;"></i>
        <i id="demo2" style="position:relative;font-size:42px!important;"></i>
    </a>
    <a href="http://www.dddd.com" class="w3-nav-item">데모</a>
'''

soup = BeautifulSoup(sample_data, 'html.parser')
print(soup.find('a')) # 태그만 사용
print(soup.find(class_='w3-nav-item')) # 속성만 사용

print(soup.find('i', id='demo2')) # 태그 + 속성 사용
