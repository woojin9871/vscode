import selenium
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains # 마우스오버기능
from selenium.webdriver.common.keys import Keys

from bs4 import BeautifulSoup

URL = 'https://ediyastore.com/index.html'

try:    
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(URL) 
    time.sleep(1) 
    
    menu_elem = browser.find_elements(By.CLASS_NAME,'xans-record-')
    
    ActionChains(browser).move_to_element(menu_elem[1]).click().perform()
    
    html_src = browser.page_source
    soup = BeautifulSoup(html_src, 'html.parser')
    
    prod_list = soup.select('.prdList .name')   
    prod_price = soup.select('.prdList .xans-element->li>span')
    
    for i in range(len(prod_price)):
            print(prod_price[i].get_text())
    
except Exception as e:
    print('에러 발생')
    
finally:
    browser.close