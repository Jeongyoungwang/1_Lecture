#
import sys
import io
import urllib.request as req

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')#아톰에서 한글 출력 할려면 필수 코드

url = "http://www.encar.com"

mem = req.urlopen(url)

print(type(mem))

print("geturl",mem.geturl()) #방금 전 요청했던 주소 반환
print("status",mem.status) #200, 404, 403, 500 #웹사이트 상태 속성
print("headers",mem.getheaders()) #서버에 대한 정보를 리스트 형식으로
print("info",mem.info()) #겟헤더스 줄바꿈해서 이쁘게
print("code",mem.getcode()) #스테이터스랑 똑같음
print("read",mem.read(50).decode("utf-8")) #euc-kr ... #저번에 썼던건데 html 정보 읽어옴 근데 정수 입력하면 적당한 부분만 가져옴 소스 낭비 안할려고
#decode는 리드랑 잘붙여서 써 문자 깨지는거 막을려고 옜날 사이트에서 쓸려면 euc-kr
