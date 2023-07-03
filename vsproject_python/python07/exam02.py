import selenium
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains # 마우스오버기능

URL = 'https://www.mcdonalds.co.kr/kor/main.do'

try :
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(URL)
    time.sleep(5)
    link_recruit = browser.find_element(By.LINK_TEXT, 'RECRUIT')
    # print(link_elem.tag_name)
    # link_elem.click()

    # 마우스를 올려서 펼치기
    div_menu = browser.find_element(By.CLASS_NAME, 'hMenu')
    
    # 서브 메뉴 클릭 (요소를 두번 거친다)
    li_depth_store = browser.find_elements(By.CSS_SELECTOR, ('.depth1>li'))
    li_depth2_store = li_depth_store[1].find_elements(By.CSS_SELECTOR, ('.depth2>li'))
    link_macDeliv = li_depth2_store[1]  
    time.sleep(3)

    action_mouseover = ActionChains(browser)
    action_mouseover.move_to_element(div_menu).perform()
    # action_mouseover.click(link_macDeliv).perform()
    link_macDeliv.click() # dropmenu -> 펼쳐지지 않음

    time.sleep(5)
except Exception as e:
    print('에러처리')    
finally:
    browser.close
