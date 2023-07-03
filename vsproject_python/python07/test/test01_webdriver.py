import selenium
from selenium import webdriver
import time

driver_path = "C:\kwj\Webdriver\chromedriver_win32"
brower = webdriver.Chrome(driver_path)

brower.get('http://www.naver.com')
time.sleep(5)