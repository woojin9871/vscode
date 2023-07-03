import requests
import re

URL = "https://euler.synap.co.kr/problem=1"

response = requests.get(URL) 
html_data = response.text

start_key = html_data.find('<div class="problem_content">')
end_key = html_data.find(' <div style="text-align:center;')
temp = html_data[start_key:end_key]
# print(temp)

mat = re.search('<p.*</p>', temp)
subject = re.sub("<.+?>", "", mat.group())
print(subject)

mat2 = re.search('<p.*</div>', temp)
subject2 = re.sub("<.+?>", "", mat2.group())
print(subject2)

num = 1
sum = 0
while(num <= 1000):
    num += 1
    if(num % 3 == 0 or num % 5 == 0):   
        sum += num
print(sum)
    