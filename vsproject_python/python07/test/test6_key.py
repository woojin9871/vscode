import selenium
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

URL = 'https://www.naver.com/'
try :
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(URL)
    time.sleep(3)
    query_win = browser.find_element(By.ID, 'query')
    query_btn = browser.find_element(By.ID, 'search_btn')
    query_win.send_keys('파이썬')
    time.sleep(1)
    query_btn.click()
    
    
    time.sleep(3)
except Exception as e:
    print('에러처리')    
finally:
    browser.close