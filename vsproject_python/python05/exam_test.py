import re
import urllib.request
import urllib.parse

# URL="https://search.daum.net/search?q="

query = '파이썬'
newquery = urllib.parse.quote('파이썬')

NEWURL = "https://search.yahoo.com/search?p=" + newquery
req = urllib.request.Request(NEWURL)
response = urllib.request.urlopen(req)
byte_data = response.read()
text_data = byte_data.decode()
print(text_data)

word = re.findall('python', text_data)
print('총 개수: ' + str(len(word)))
print(word)