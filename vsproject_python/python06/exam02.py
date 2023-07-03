# URL = "https://www.top50glasses.com/shop/index/"
# 타이틀 제목을 출력하시오
from bs4 import BeautifulSoup
import requests

URL = "https://www.top50glasses.com/shop/index/"
response = requests.get(URL)
html_data = ""
if(response.status_code==200):
    html_data = response.text
html_data = response.text
# print(html_data.find('으뜸50안경 쇼핑몰'))

soup = BeautifulSoup(html_data, 'html.parser')
# print(soup.prettify())
print(soup.title)

