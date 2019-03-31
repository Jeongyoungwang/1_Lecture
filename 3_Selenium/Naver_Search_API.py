import sys
import io
from selenium import webdriver
import time
from bs4 import BeautifulSoup


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


class NaverSearch:
    #초기화 실행(webdriver 설정)

    def __init__(self):
        self.driver = webdriver.Chrome('webdriver\chrome\chromedriver')  #셀레니움 생으로
        self.driver.set_window_size(1280,800)


    # cli
    #    chrome_options = Options()
    #    chrome_options.add_argument("--headless") #CLI (User-agent)
    #    self.driver = webdriver.Chrome(chrome_options=chrome_options,executable_path="webdriver\chrome\chromedriver")

    #네이버 광고 로그인 && 키워드 도구
    def NaverSearch(self):
        self.driver.get('https://searchad.naver.com/login?returnUrl=https%3A%2F%2Fmanage.searchad.naver.com%2F')
        time.sleep(0.3)
        self.driver.find_element_by_name('id').send_keys('sumer3')
        time.sleep(0.3)
        self.driver.find_element_by_name('pw').send_keys('korscu2')
        time.sleep(0.3)
        self.driver.find_element_by_xpath('//*[@id="container"]/div/div/fieldset/div/span/button').click()
        time.sleep(0.3)
        self.driver.implicitly_wait(30)
        self.driver.get('https://manage.searchad.naver.com/customers/1139044/tool/keyword-planner')
        time.sleep(0.3)
        self.driver.find_element_by_xpath('//*[@id="wrap"]/div/div/div[1]/div[1]/div/div/div/div[2]/div[1]/div[1]/div[2]/form/div[1]/div/div/textarea').send_keys('김밥')
        time.sleep(0.3)
        self.driver.find_element_by_xpath('//*[@id="wrap"]/div/div/div[1]/div[1]/div/div/div/div[2]/div[1]/div[1]/div[2]/form/div[4]/div/div/ul/li/button/span').click()
        self.driver.implicitly_wait(30)
        self.driver.get('https://manage.searchad.naver.com/keywordstool?format=json&siteId=&mobileSiteId=&hintKeywords=%EA%B9%80%EB%B0%A5&includeHintKeywords=0&showDetail=1&biztpId=&mobileBiztpId=&month=&event=&keyword=')
        self.driver.switch_to_frame
    #뷰티플수프
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        print(soup.prettify())



#실행


if __name__ == '__main__':
    #객체 생성
    a = NaverSearch()
    #시작 시간
    start_time = time.time()
    #프로그램 실행
    a.NaverSearch()
