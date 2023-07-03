import json
import requests
import save_token

# 저장된 토큰 정보를 읽어 옴
tokens = save_token.load_tokens(save_token.KAKAO_TOKEN_FILE)


# json 문자열의 '(작은따옴표)를 "(큰따옴표)로 변환
json_str = tokens.replace("'", "\"")

# # json 문자열을 딕셔너리 변환
tokens = json.loads(json_str)
print(json_str)

# print(tokens)
print(tokens['access_token'])

# 텍스트 메시지 url
# 카카오톡 나에게 보내기
url = 'https://kapi.kakao.com/v2/api/talk/memo/default/send'

# header 정보
# Authorization : 인증 정보를 담는 헤더
headers = {
    'Authorization' : 'Bearer ' + tokens['access_token']    
}

temp = {
    'object_type' : 'feed',     # text, feed
    # 'text' : '안녕 유튜브~!',
    # URL 은 Kakao Developer > 내 애플리케이션 > 앱설정 > 플랫폼 > web 에
    # 등록된 도매인만 사용가능합니다.
    "content" : {
        "title" : "정대만",
        "description" : "포기를 모르는 남자지",
        "image_url": "https://file.mk.co.kr/mkde/N0/2016/03/201603080305561821779.jpg",
        "image_width": 640,
        "image_height": 640,
        
        'link' : { 
                    "web_url" : 'www.naver.com',                # PC 카톡의 URL
                    "mobile_web_url" : "https://m.youtube.com"  # 모바일 URL
                }
    }
}

data = {
    'template_object' : json.dumps( temp )
}

# 나에게 카카오 메시지 보내기
response = requests.post(url, headers=headers, data=data)
print(response.status_code)