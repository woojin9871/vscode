import requests
import re

URL="https://www.nate.com/?f=news"
response = requests.get(URL)
html_data = response.text
print(html_data)

# start_idx = html_data.find('<div class="bizCnt">')
# print(html_data[start_idx:start_idx+500])

# 2단계
start_sub = html_data.find('<div class="isKeyword">')
print(start_sub)
end_sub = html_data.find('<ol class="isKeywordList"')
print(end_sub)
temp2 = html_data[start_sub:end_sub]
mat = re.search("<h4.*/h4>", temp2)
subject = re.sub("<.+?>", "", mat.group())
print(subject)

# 3단계
start_key = html_data.find('<div class="isKeyword">')
end_key = html_data.find('<form id="frmKeyword"')
temp3 = html_data[start_key:end_key]
# print(temp3.split('<li>')[0])
LENGTH = len(temp3.split('<li>'))
#print(LENGTH) # 0~5 => 1~5

# 1~5 위 아니면 6~10위
mat = re.search('<span class="num_rank".*/span>', 
temp3.split('<li>')[1])
num = re.sub('<.+?>', '', mat.group())
print('등수='+num)

for x in range(1, LENGTH):
    mat = re.search('<span class="num_rank".*/span>', 
    temp3.split('<li>')[x])
    num = re.sub('<.+?>', '', mat.group())

    mat2 = re.search('<span class="txt_rank".*/span>', 
    temp3.split('<li>')[x])
    txt = re.sub('<.+?>', '', mat2.group())
    print(num + "위 : " + txt)


