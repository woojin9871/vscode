import urllib.request

URL = 'https://cheese10yun.github.io/'
urllib.request.urlopen(URL)
response = urllib.request.urlopen(URL)
byte_data = response.read()
# print(byte_data)  # 바이너리 데이터를
f = open("blog.hmtl", 'wb')
f.write(byte_data)
f.close
