import sys
import io
from bs4 import BeautifulSoup
import requests

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#로그인 유저정보
LOGIN_INFO = {
    'user_id': 'sumer3',
    'user_pw': 'korscu2-'
}

#Session 생성, with 구문안에서 유지
with requests.Session() as s:
    login_req = s.post('https://user.ruliweb.com/member/login_proc',data=LOGIN_INFO)
    #HTML 소스 확인
    #print('login_req',login_req.text)
    #Header 확인
    #print('headers',login_req.headers)
    if login_req.status_code == 200 and login_req.ok:
        post_one = s.get('http://market.ruliweb.com/read.htm?table=market_etc&page=1&num=325344&find=subject&ftext=')
        post_one.raise_for_status()
        soup = BeautifulSoup(post_one.text, 'html.parser')
        #print(soup.prettify())
        article = soup.select_one("table:nth-of-type(3)").find_all('p')
        #print(article)
        for i in article:
            if i.string is not None:
                #DB INSERT , 엑셀로 저장, 텍스트 가공
                print(i.string)
