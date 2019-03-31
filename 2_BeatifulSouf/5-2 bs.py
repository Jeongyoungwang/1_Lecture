
from bs4 import BeautifulSoup

#직접접근 access that dictionary directly, 실제 사용빈도는 낮지만 bs4문서에 나왔으니 기본적으로 알아두자.

import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
#한글 인코딩 위한 필수 코드

#html 가져올려면 1.웹 url리트리브 쓰면됨 2.하드디스크 3.아톰에서 만들어낼 수도 있어

#줄바꿈 세개
html = """
<html>
<body>
<h1>파이썬 BeautifulSoup 공부</h1>
<p>태그 선택자</p>
<p>css 선택자</p> ☆☆☆☆☆☆☆
</body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser') #뷰티플수프 객체 초기화
#첫번째 인자로 html을 받고, parser 설정

print(type(soup), '<-soup객체타입' )
print("\n-----------------")
print(soup.prettify(), '<-prettify사용') #이쁘게 전체 출력-나중에 길어지니 웹브라우저로 하는게 효율
print("\n-----------------")

h1 = soup.html.body.h1 #요지는 점을 찍으면서 쓴다는것
print('h1',h1)
p1 = soup.html.body.p
print('p1',p1)
p2 = p1.next_sibling.next_sibling #/d 줄바꿈으로 인식되어서 두번 해줘야함, 별로 사용안됨
print('p2',p2)
p3 = p1.previous_sibling.previous_sibling
print('p3',p3)

print("\n-----------------")

print("h1 >> ",h1.string)
print("p >>  ",p1.string)
print("p >>  ",p2.string)
