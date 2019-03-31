#태그 선택자? 암튼 많이쓰이긴 함
from bs4 import BeautifulSoup

import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
#한글 인코딩 위한 필수 코드

html = """
<html><body>
    <ul>
        <li><a href="http://www.naver.com">naver</a></li>
        <li><a href="http://www.daum.net">daum</a><li>
        <li><a href="http://www.daum.com">daum</a><li>
        <li><a href="https://www.google.com">google</a><li>
        <li><a href="https://www.tistory.com">tistory</a></li>
    </ul>
</body></html>
"""
print("-----links타입------")
soup = BeautifulSoup(html, 'html.parser') #html 파싱하겠다고 선언

#많이 쓰는 태그 선택자 find all
links = soup.find_all("a") #해당 엘리먼트를 한번에 가져와 여기선 a태그를 한번에 가져오기
print(type(links), '← links타입',)
print("\n-----for문 && href, txt------")

for a in links:
    print(a)
#위에거만으로 for문 동작함
    href = a.attrs['href']
    txt = a.string
    print('txt >> ',txt, 'href >> ',href)

print("\n----스트링이 다음 노드인것만 가져오기-------")
a = soup.find_all("a",string="daum")
print(a, '← a')

b = soup.find_all("a", limit=3) #limit=0
print(b,'← b')

c = soup.find_all(string=["naver", "google"]) #string만 찾아오기
print(c,'← c') #해당 내용 가져옴
print(type(c), '← c타입')
