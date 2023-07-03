from konlpy.tag import Okt

# 객체 생성
okt = Okt()

word = okt.morphs("와우 오늘 봤던 영화가 흥미롭고 재미있네", stem=True)

print(word)

