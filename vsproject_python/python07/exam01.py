'''
    URL = "https://map.kakao.com/"
    selenium 모듈을 사용하여 다음 테그를 찾아 출력하시오
        <form id="search.keyword">
'''

import selenium
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

try:
    URL = "https://map.kakao.com/"
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(URL)
    myelement = browser.find_element(By.ID, 'search.keyword')
    time.sleep(5)
except Exception as e:
    print('에러처리')
finally:
    browser.close

