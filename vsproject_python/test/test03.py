'''
    URL = "https://search.shopping.naver.com/best/home?
           categoryCategoryId=ALL&categoryDemo=A00&
           categoryRootCategoryId=ALL&chartDemo=A00&chartRank=1&period=P1D&
           windowCategoryId=20000049&windowDemo=A00&windowRootCategoryId=20000049"
           
    쇼핑 트랜드 차트 사이트를 웹크롤링 해서
    순위 1~5위와 이름을 가져와서 데이터를 출력하시오
'''
import requests
import re

URL = "https://search.shopping.naver.com/best/home?categoryCategoryId=ALL&categoryDemo=A00&categoryRootCategoryId=ALL&chartDemo=A00&chartRank=1&period=P1D&windowCategoryId=20000055&windowDemo=A00&windowRootCategoryId=20000059"
# params = {'categoryCategoryId' : 'ALL',
#           'categoryDemo' : 'A00',
#           'categoryRootCategoryId' : 'ALL',
#           'chartDemo' : 1,
#           'period' : 'P1D',
#           'windowCategoryId' : 20000049,
#           'windowDemo' : 'A00',
#           'windowRootCategoryId' : 20000049
#           }
response = requests.get(URL) # , params=params
html_data = response.text

# end = html_data.find('6위 ~ 10위')

start_key = html_data.find('<h2 class="home_title__4lcuB">')
temp2 = html_data[start_key:start_key+100]
mat = re.search("<h2.*/h2>", temp2)
subject = re.sub("<.+?>", "", mat.group())
print(subject)

start_key2 = html_data.find('쇼핑 트렌드 차트')
# print(start_key2)
end_key2 = html_data.find('6위 ~ 10위') 
# print(end_key2)
temp3 = html_data[start_key2:end_key2]
LENGTH = len(temp3.split('<li '))
# print(LENGTH) # 0~5 => 1~5

mat = re.search('<span class="chartList_rank__ZTvTo".*<span class="blind">위</span>', 
temp3.split('<li ')[1])
num = re.sub('<.+?>', '', mat.group())
print('등수')

for x in range(1, LENGTH):
    mat = re.search('<span class="chartList_rank__ZTvTo".*<span class="blind">위</span>', 
    temp3.split('<li ')[x])
    num = re.sub('<.+?>', '', mat.group())

    mat2 = re.search('</em>.*<span class="chartList_toggle__cQZC_">', 
    temp3.split('<li ')[x])
    txt = re.sub('<.+?>', '', mat2.group())
    print(num + ": " + txt)


