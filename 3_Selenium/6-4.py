import sys
import io
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#chrome_options = Options()
#chrome_options.add_argument("--headless") #CLI

#driver = webdriver.Chrome(chrome_options=chrome_options,executable_path='webdriver\chrome\chromedriver')
driver = webdriver.Chrome('webdriver\chrome\chromedriver')
driver.implicitly_wait(3)

driver.get('https://www.inflearn.com/wp-login.php?redirect_to=https%3A%2F%2Fwww.inflearn.com%2F')
time.sleep(7)
driver.implicitly_wait(3)

driver.find_element_by_name('log').send_keys('sumer3')
driver.implicitly_wait(1)
driver.find_element_by_name('pwd').send_keys('qerwqerqw')
driver.implicitly_wait(1)
driver.find_element_by_xpath('//*[@id="wp-submit"]').click()




print('스크린샷 완료')
