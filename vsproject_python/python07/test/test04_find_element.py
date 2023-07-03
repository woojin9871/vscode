# 한개 요소를 찾을 때

import selenium
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By #변경함수때문에

try: 
    browser = webdriver.Chrome(ChromeDriverManager().install())
    URL = 'https://www.naver.com'
    browser.get(URL)
    time.sleep(5)
    # 작업한 내용 에러가 생기면
    element = browser.find_element(By.ID, 'account')
    print(element.tag_name)

except Exception as e:
    # 에러처리 후 
    print('에러출력')
finally:    
    browser.close



