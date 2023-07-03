import urllib.request

WEB_IMG_URL = 'https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Ft1.daumcdn.net%2Fcfile%2Ftistory%2F99B0764A5BD3C83C24'
WEB_HTML_URL = 'https://movie.naver.com/movie/running/current.naver?view=list&tab=normal&order=point'
# 기본 경로는 파이썬 프로젝트 폴더 vsproject_python
PC_IMG_PATH = ''
PC_IMG_SAVE = 'china_map.jpg'
PC_HTML_SAVE = 'movie.html'

urllib.request.urlretrieve(WEB_IMG_URL, PC_IMG_SAVE)
urllib.request.urlretrieve(WEB_HTML_URL, PC_HTML_SAVE)