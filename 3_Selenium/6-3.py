import sys
import io
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

firefox_options = Options()
firefox_options.add_argument("--headless") #CLI

driver = webdriver.Firefox(firefox_options=firefox_options,executable_path='webdriver\Firefox\geckodriver')

#driver.implicitly_wait(5)

driver.get('https://google.com')
#time.sleep(5)

driver.save_screenshot("C:\websitef1.png")

#driver.implicitly_wait(5)

driver.get('https://www.daum.net')
#time.sleep(5)
driver.save_screenshot("C:\websitef2.png")

driver.quit()

print('스크린샷 완료')
