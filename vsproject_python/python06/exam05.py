'''
    select 또는 select_all(선택자)를 사용해서 검색하기
        1. <button class...>
        2. <ul class=...>           ul>li
        3. <li class="nav-item">    li img   
        4. <li class="nav-item">    nav-item 클래스명
'''
from bs4 import BeautifulSoup
import requests

html_data = '''
<button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <a class="px-0 nav-link position-relative" href="/shop/order/cart.php">
                    <img src="/shop/_images/icons/shopping-bag.svg"/>
                    <span class="badge badge-counter rounded-pill bg-primary-1">0</span>
                </a>
            </button>
            <div class="collapse navbar-collapse main-menu ps-2 ps-xl-2 ms-2 ms-xl-2" id="navbarSupportedContent">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0 mt-2">
                    <li class="nav-item px-1 px-xl-2">
                        <a class="nav-link active" aria-current="page" href="../goods/best.php">베스트</a>
                    </li>
                    <li class="nav-item px-1 px-xl-2">
                        <a class="nav-link" href="../goods/new.php">신상품</a>
                    </li>
                    <li class="nav-item px-1 px-xl-2">
                        <a class="nav-link" href="../event/">이벤트</a>
                    </li>
                    <li class="nav-item px-1 px-xl-2">
                        <a class="nav-link" href="/store/store_search.php" target="_blank">지점 찾기</a>
                    </li>
                    <li class="nav-item px-1 px-xl-2">
                        <a class="nav-link" href="/" target="_blank">으뜸50안경홈</a>
                    </li>
                </ul>
                <ul class="top-icons navbar-nav mb-2 mb-lg-0 d-flex mt-2">
                    <li class="nav-item">
                        <a type="button" class="btn btn-link" data-bs-toggle="modal" data-bs-target="#modal_product_search">
                            <img src="/shop/_images/icons/search.svg"/>
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="px-1 px-xl-2 nav-link" href="/?a=login"><img src="/shop/_images/icons/user.svg"/></a>
                    </li>
                    <li class="nav-item">
                        <a class="px-1 px-xl-2 nav-link position-relative" href="/?a=login">
                            <img src="/shop/_images/icons/heart.svg"/>
                                                   </a>
                    </li>
                    <li class="nav-item">
                        <a class="px-1 px-xl-2 nav-link position-relative" href="/?a=login">
                            <img src="/shop/_images/icons/shopping-bag.svg"/>
                                                    </a>
                    </li>
                </ul>
            </div>
'''

soup = BeautifulSoup(html_data, 'html.parser')
# print(soup.prettify())
# print(soup.select_one('button'))
# print(soup.select('ul>li'))
# print(len(soup.select('ul>li')))
# print(soup.select('li img'))
# print(soup.select_one('.nav-item'))
