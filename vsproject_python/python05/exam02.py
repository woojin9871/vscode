import re
# 가져온 html_data
html_data = "<div><p><a>python</a></p><ul><li>python</li></ul></div>"
word = re.findall('python', html_data)
print('총갯수: ' + str(len(word)))
print(word)

