import sys
import io
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

class NaverAd:
    #초기화 실행(webdriver 설정)
    def _init_(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless") #CLI (User-agent)
        self.driver = webdriver.Chrome(chrome_options=chrome_options,executable_path="webdriver\chrome\chromedriver")
        self.driver.implicitly_wait(5)

    #네이버 카페 로그인 && 출석 체크
    def writeAttendeCheck(self):
        self.driver.get('https://searchad.naver.com/login?returnUrl=https%3A%2F%2Fmanage.searchad.naver.com%2F')
        self.driver.find_element_by_name('id').send_keys('sumer3')
        self.driver.find_element_by_name('pw').send_keys('korscu2')
        self.driver.find_element_by_xpath('//*[@id="container"]/div/div/fieldset/span/button').click()
        self.driver.implicitly_wait(30)
        self.driver.get('https://manage.searchad.naver.com/customers/1139044/tool/keyword-planner') #구닥넷 출석부 url주소 넣어야함
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_class_name('btn-group').send_keys('반갑습니다')
        self.driver.find_element_by_xpath('//*[@id="wrap"]/div/div/div[1]/div[1]/div/div/div/div[2]/div[1]/div[1]/div[2]/form/div[4]/div/div/ul/li/button').click
        time.sleep(3)

    # 소멸자
    def __del__(self):
        #self.driver.close() #현재 실행 포커스된 영역 종료
        self.driver.quit() #셀레니움 전체 프로그램 종료
        print("Removed driver Object")
#실행
if __name__=='_main_':
    #객체 생성
    a = NaverAd()
    #시작 시간
    start_time = time.time()
    #프로그램 실행
    a.writeAttendCheck()
    #종료 시간 출력
     print("---Total %s seconds ---" % (time.time() - start_time))
     #객체 소멸
     del a
