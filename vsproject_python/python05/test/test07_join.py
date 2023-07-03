import urllib.request
import urllib.parse

URL = "https://www.nate.com/aaa/bbb"

parse = urllib.parse.urlparse(URL)
print(parse)
newURL = urllib.parse.urljoin(URL+'', 'ccc')
# 앞에 패스에 / 가 없다면 마지막 패스가 치환
# 앞에 패스에 / 가 있다면 유지한채로 결합
print(newURL)

newURL2 = urllib.parse.urljoin(URL, '/ccc')
# 패스 앞에 / 를 붙이면 루트라는 의미가 있다
# 패스 앞에 ./ 를 붙이면 현재 패스라는 의미가 있다
# 패스 앞에 ../ 를 붙이면 상위 패스라는 의미가 있다
print(newURL2)