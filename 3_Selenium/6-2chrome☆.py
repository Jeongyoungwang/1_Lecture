import sys
import io
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

chrome_options = Options()
chrome_options.add_argument("--headless") #CLI  ☆☆☆☆☆☆☆☆☆☆☆

driver = webdriver.Chrome(chrome_options=chrome_options,executable_path='webdriver\chrome\chromedriver')
#driver = webdriver.Chrome('webdriver\chrome\chromedriver')  #셀레니움 생으로
#driver.set_window_size(1280,800)
#driver.implicitly_wait(5)

driver.get('https://google.com')
#time.sleep(5)

driver.save_screenshot("C:\website4.png")

#driver.implicitly_wait(5)

driver.get('https://www.daum.net')
#time.sleep(5)
driver.save_screenshot("C:\website5.png")

driver.quit()

print('스크린샷 완료')
