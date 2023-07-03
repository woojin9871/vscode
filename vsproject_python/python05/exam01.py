# URL="http://kbsart.co.kr/kr/program/program_list.asp"
# 국군의 날 1.png 추출해서 이미지를 다운로드 하시오

# 힌트 : 이미지 태그를 찾는 정규식을 사용하세요

# import urllib.request
# import urllib.parse
import requests
import re

text='<div class="img"><img src="http://kbsart.co.kr/data/onlinedata/국군의날 1.png" alt="[행사] 제73주년 국군의 날 이미지"></div>'
re_img = re.compile("<[Ii][Mm][Gg]\s+[^>]+>", re.MULTILINE)
img_tag = re_img.findall(text)
print(img_tag)

# URL = "http://kbsart.co.kr/data/onlinedata/%EA%B5%AD%EA%B5%B0%EC%9D%98%EB%82%A0%201.png"
# PC_IMG_PATH = ""
# PC_IMG_SAVE = '국군의 날1.png'

# urllib.request.urlretrieve(URL, PC_IMG_SAVE)
