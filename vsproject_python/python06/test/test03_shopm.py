import requests
from bs4 import BeautifulSoup

# html data 가져오기
URL = "https://rounz.com/home.php"
response = requests.get(URL)
html_data = ""
if(response.status_code==200):
    hmtl_data = response.text
html_data = response.text
# print(html_data.find('지금 가장 핫한 상품'))

soup = BeautifulSoup(html_data, 'html.parser')
# print(soup.prettify())
print(soup.title)
    