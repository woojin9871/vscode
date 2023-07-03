import selenium
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains # 마우스오버기능
from selenium.webdriver.common.keys import Keys

from bs4 import BeautifulSoup

URL = 'https://ediyastore.com/index.html'

try :
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(URL)
    time.sleep(3)

    menu_elem = browser.find_elements(By.CLASS_NAME, 'xans-record-')
    # print(menu_elem[1].text)
    menu_elem[1].click()
    
    html_src = browser.page_source
    # bs4 모듈을 사용해서 가져옵니다
    soup = BeautifulSoup(html_src, 'html.parser')
    # print(soup.prettify())
    prod_list = soup.select('.prdList .name')
    for i in range(len(prod_list)): 
        print(prod_list[i].get_text())
    
    # bs4 모듈 적용 끝

    time.sleep(3)

except Exception as e:
    print('에러처리')    
finally:
    browser.close()       