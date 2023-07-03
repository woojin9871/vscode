import requests
import re

# 1단계
URL = "https://datalab.naver.com/"
response = requests.get(URL)
html_data = response.text
print(html_data)

# 2단계
start_title = html_data.find('<a href="#" class="select_btn">')
temp1 = html_data[start_title:start_title+50]
mat = re.search('<a.*/a>', temp1)
title = re.sub('<.+?>', '', mat.group())
print(title)

#3단계 - 가공1
start_date = html_data.find('<div class="keyword_carousel">')
end_date = html_data.find('<div class="keyword_notice">')
temp2 = html_data[start_date:end_date]
LENGTH = len(temp2.split('<div class="keyword_rank">'))
#print(LENGTH)
temp3_html = temp2.split('<div class="keyword_rank">')[LENGTH-1]
# print(temp3_html.find('<span class="title_cell">'))
mat3 = re.search('<span class="title_cell".*/span>', temp3_html)
data_result = re.sub('<+?>', '', mat3.group())
print(data_result)

# 3단계 - 가공2 (반복출력)
LI_LENGTH = len(temp3_html.split('<li class="list">'))

for n in  range(1, LI_LENGTH-1):
    temp4_li = temp3_html.split('<li class="list">')[n]
    mat4 = re.search('<em class="num".*/em>', temp4_li)
    num_result = re.sub('<.+?>', '', mat4.group())
    print(num_result + "위 : ")
    mat4 = re.search('<span class="title".*/span>', temp4_li)
    txt_result = re.sub('<.+?>', '', mat4.group())
    print(txt_result)
    
