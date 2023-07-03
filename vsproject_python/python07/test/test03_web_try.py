import selenium
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

try:
    browser  = webdriver.Chrome(ChromeDriverManager())
    URL = "https://www.naver.com"
    browser.get(URL)
    time.sleep(5)
    # 작업한 내용 에러가 생기면
except Exception as e:
    # 에러처리 후
    print('에러출력')
finally:
    browser.close