import selenium
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

URL = 'https://www.naver.com/'
try :
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(URL)
    time.sleep(5)
    dict_elem = browser.find_element(By.CSS_SELECTOR, ('.NM_FAVORITE_LIST>li'))
    # 첫번째만 가져옴
    dict_elem.click()
    time.sleep(5)

    # move_to_element(element)

except Exception as e:
    print('에러처리')    
finally:
    browser.close    