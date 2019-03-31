#대망의 css 선택자 ☆☆☆☆☆ -select로 호출

from bs4 import BeautifulSoup

import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
#한글 인코딩 위한 필수 코드

html = """
<html><body>
<div id="main">
    <h1>강의목록</h1>
    <ul class="lecs">
        <li>Java 초고수 되기</li>
        <li>파이썬 기초 프로그래밍</li>
        <li>파이썬 머신러닝 프로그래밍</li>
        <li>안드로이드 블루투스 프로그래밍</li>
    </ul>
</div>
</body></html>
"""

soup = BeautifulSoup(html, 'html.parser')
h1 = soup.select_one("#main > h1") #명시적으로 di 태그 붙여도 됨
print('h1',h1.string) #가져올 노드 하나면 셀렉트 원
#노드 ?? #아래거랑 별개임

list_li = soup.select("#main > ul.lecs > li") #셀렉트 반복문  셀-원 걍 프린트
for li in list_li:
    print("li >>>", li.string)
