import requests # 서버에 html 요청
from bs4 import BeautifulSoup
import urllib.request
import urllib.parse

# html소스를 받아옴
URL="http://kbsart.co.kr/kr/business/business_list.asp"
response = requests.get(URL)
html_data = response.text

# img src 검색
soup = BeautifulSoup(html_data, 'html.parser')
html_div = soup.find('div', class_='work-con03')
html_img = html_div.find_all('img')
attr_src = html_img[0].get('src')

# print(attr_src)
# new_src = urllib.parse.quote(attr_src)
# print(new_src)

# 다운로드 전에 한글명 -> 퍼센트인코딩
korean_img = urllib.parse.urlparse(attr_src)
new_path = urllib.parse.quote(korean_img.path)
korean_img = list(korean_img)
korean_img[2] = new_path
new_korean_img = urllib.parse.urlunparse(korean_img)

# 변경된 경로명을 사용해서 이미지 다운로드
# for img_src in html_img:
#     print(img_src.get('src'))
img_down = "test.jpg"
urllib.request.urlretrieve(new_korean_img, img_down)