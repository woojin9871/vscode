from bs4 import BeautifulSoup
import requests

html_data = '''
<div class="container d-none d-lg-block">
        <ul class="nav sub-menu pb-3 pt-2">
            <li class="nav-item">
                <a class="nav-link active" aria-current="page" href="../goods/?category=10">안경테</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="../goods/?category=11">선글라스</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="../goods/?category=12">콘택트렌즈</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="../goods/?category=13">기타</a>
            </li>
        </ul>
    </div>
'''


soup = BeautifulSoup(html_data, 'html.parser')
# print(soup.prettify())
# print(soup.select_one('ul'))      # 태그
# print(soup.select_one('ul>li'))   # 부모 > 직계자녀
# print(soup.select_one('ul a'))    # 부모 자녀,지손들
# print(soup.select_one('#mymenu'))   # 아이디
print(soup.select('.nav-link'))


