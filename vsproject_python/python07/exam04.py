import selenium
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains # 마우스오버기능
from selenium.webdriver.common.keys import Keys

URL = 'https://www.ediya.com'

try :
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(URL)
    time.sleep(3)
    nav_main_elem = browser.find_element(By.CLASS_NAME, 'main')
    sub_elem = browser.find_elements(By.CLASS_NAME, 'sub')
    li_elem = sub_elem[5].find_element(By.CSS_SELECTOR, 'a')
    # print(li_elem[1].get_attribute('innerText'))
    # print(li_elem.get_attribute('innerHTML'))
      
    action_nav = ActionChains(browser)
    action_nav.move_to_element(nav_main_elem).perform()
    time.sleep(1)
    # li_elem[1].click() # a태그 링크만 있는 경우 - 자바스크립트 같이 이벤트
    li_elem[1].send_keys(Keys.RETURN)
    time.sleep(3)

    # 복습
    # sub_elem = browser.find_elements(By.CLASS_NAME, 'sub')
    # li_elem = sub_elem[0].find_element(By.TAG_NAME, 'li')
    # print(li_elem.get_attribute('innerText'))
except Exception as e:
    print('에러처리')    
finally:
    browser.close()    