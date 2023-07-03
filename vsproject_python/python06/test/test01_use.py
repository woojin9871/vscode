from bs4 import BeautifulSoup

# html_data = '<head><title>홈페이지</title></head>' #requests 가져온 데이터
html_data = '''
    <ul class="seum_top_box_l">
    <li><a href="../member/join_method.php">JOIN</a>
        <!--<span class="accent">
            <span><strong>2,000 P</strong></span>
        </span>-->
    </li>
    <li><a href="../member/login.php">LOGIN</a></li>
    <li><a href="../mypage/index.php">MYPAGE</a></li>
    <li><a href="../order/cart.php">CART</a></li>
    <li class="dn">
        <div class="top_mypage_cont">
            <span class="top_mypage_tit"><a href="../mypage/index.php">MYPAGE</a></span>
            <ul style="display:none;">
                <li><a href="../mypage/order_list.php">주문조회</a></li>
                <li><a href="../mypage/my_page_password.php">내정보수정</a></li>
                <li><a href="../mypage/wish_list.php">찜 리스트</a></li>
                <li><a href="../mypage/mypage_qa.php">1:1 문의</a></li>
            </ul>
        </div>
    </li>
    <li class="dn"><a href="../order/cart.php">장바구니( <strong>0</strong> )</a></li>
    <li class="dn"><a href="../service/index.php">고객센터</a></li>
</ul>
'''
#객체지향으로 인스턴스변수를 선언
soup = BeautifulSoup(html_data, 'html.parser')
# print(html_data)
print(soup.prettify())
