# 네이버 주요 뉴스 15개 뉴스글자만 뽑아서 출력

from bs4 import BeautifulSoup

html_data = '''
<div class="section" style="margin-bottom:20px; white-space:nowrap;" id="right_dailyList"> 
 <h4>분야별 주요뉴스</h4> 
 <div class="classfy sd" style="display:block"> 
  <ul class="list_txt"> 
   <li> <a href="https://n.news.naver.com/mnews/article/056/0011427318?sid=100" class="nclicks(rig.secteco)" title="[속보] 박홍근 “김건희 여사 주가조작 의혹 ‘국민특검’ 반드시 관철”">[속보] 박홍근 “김건희 여사 주가조작 의혹 ‘국민특검’ 반드시 관철”</a> </li> 
   <li> <a href="https://n.news.naver.com/mnews/article/001/0013752441?sid=100" class="nclicks(rig.secteco)" title="尹지지율, 2.4%p 내린 36.9%…부정평가 60%대로[리얼미터]">尹지지율, 2.4%p 내린 36.9%…부정평가 60%대로[리얼미터]</a> </li> 
   <li> <a href="https://n.news.naver.com/mnews/article/018/0005423495?sid=100" class="nclicks(rig.secteco)" title="홍준표, 곽상도 무죄에 연일 비판…&quot;이러니까 검수완박&quot;">홍준표, 곽상도 무죄에 연일 비판…&quot;이러니까 검수완박&quot;</a> </li> 
   <li> <a href="https://n.news.naver.com/mnews/article/081/0003338829?sid=104" class="nclicks(rig.secteco)" title="중국도 “미확인 비행체 발견” 맞불…미국은 4번째 격추">중국도 “미확인 비행체 발견” 맞불…미국은 4번째 격추</a> </li> 
   <li> <a href="https://n.news.naver.com/mnews/article/366/0000876952?sid=104" class="nclicks(rig.secteco)" title="“강진 튀르키예 경제 손실 107조 원…GDP 10% 수준”">“강진 튀르키예 경제 손실 107조 원…GDP 10% 수준”</a> </li> 
  </ul> 
  <ul class="list_txt"> 
   <ul class="list_txt"> 
    <li> <a href="https://n.news.naver.com/mnews/article/018/0005423564?sid=101" class="nclicks(rig.secteco)" title="삼성전자, 전국 삼성 디지털프라자서 ‘혼수&middot;이사 특별 기획전’ 연다">삼성전자, 전국 삼성 디지털프라자서 ‘혼수&middot;이사 특별 기획전’ 연다</a> </li> 
    <li> <a href="https://n.news.naver.com/mnews/article/437/0000332030?sid=101" class="nclicks(rig.secteco)" title="2월 1~10일 수출 11.9% 늘어…무역 적자 50억달러">2월 1~10일 수출 11.9% 늘어…무역 적자 50억달러</a> </li> 
    <li> <a href="https://n.news.naver.com/mnews/article/014/0004968135?sid=101" class="nclicks(rig.secteco)" title="'톡신분쟁' 휴젤 &quot;메디톡스-대웅 재판, 당사와 무관해&quot;">'톡신분쟁' 휴젤 &quot;메디톡스-대웅 재판, 당사와 무관해&quot;</a> </li> 
    <li> <a href="https://n.news.naver.com/mnews/article/648/0000013801?sid=105" class="nclicks(rig.secteco)" title="야놀자&middot;여기어때 '어쩌나'…카톡 선물하기에 호텔 입점한다">야놀자&middot;여기어때 '어쩌나'…카톡 선물하기에 호텔 입점한다</a> </li> 
    <li> <a href="https://n.news.naver.com/mnews/article/003/0011688469?sid=105" class="nclicks(rig.secteco)" title="네이버, 튀르키예&middot;시리아 지진 피해 복구에 100만 달러 기부">네이버, 튀르키예&middot;시리아 지진 피해 복구에 100만 달러 기부</a> </li> 
   </ul> 
   <ul class="list_txt"> 
    <ul class="list_txt"> 
     <li> <a href="https://n.news.naver.com/mnews/article/003/0011688457?sid=102" class="nclicks(rig.secteco)" title="전장연-지하철공사, 승강장 바닥에 붙은 선전물 놓고 '충돌' [뉴시스Pic]">전장연-지하철공사, 승강장 바닥에 붙은 선전물 놓고 '충돌' [뉴시스Pic]</a> </li> 
     <li> <a href="https://n.news.naver.com/mnews/article/087/0000951951?sid=102" class="nclicks(rig.secteco)" title="[속보]실내마스크 해제 보름째 코로나19 신규확진 5,174명…작년 6월 이후 최소">[속보]실내마스크 해제 보름째 코로나19 신규확진 5,174명…작년 6월 이후 최소</a> </li> 
     <li> <a href="https://n.news.naver.com/mnews/article/003/0011688407?sid=102" class="nclicks(rig.secteco)" title="인천항 항만배후단지 지난해 물동량 56만5천TEU로 사상 최대">인천항 항만배후단지 지난해 물동량 56만5천TEU로 사상 최대</a> </li> 
     <li> <a href="https://n.news.naver.com/mnews/article/421/0006626940?sid=103" class="nclicks(rig.secteco)" title="현대차그룹, 美 전기차 누적 10만대 팔았다…&quot;올해만 13만대 목표&quot;">현대차그룹, 美 전기차 누적 10만대 팔았다…&quot;올해만 13만대 목표&quot;</a> </li> 
     <li> <a href="https://n.news.naver.com/mnews/article/662/0000014399?sid=103" class="nclicks(rig.secteco)" title="문화체육관광부, 전 세계에 K-SOOL 매력 알린다">문화체육관광부, 전 세계에 K-SOOL 매력 알린다</a> </li> 
    </ul> 
   </ul>
  </ul>
 </div> 
</div>
'''

soup = BeautifulSoup(html_data, 'html.parser')
print(soup.prettify())
print(soup.select('ul>li'))