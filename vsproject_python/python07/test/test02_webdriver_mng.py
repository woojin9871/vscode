import selenium
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
browser = webdriver.Chrome(ChromeDriverManager().install())

URL = 'http://www.naver.com'
browser.get(URL)

time.sleep(5)
