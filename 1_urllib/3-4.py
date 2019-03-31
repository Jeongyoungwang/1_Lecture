import sys
import io
import urllib.request as req
from urllib.parse import urlencode
#행정안정부
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')#아톰에서 한글 출력 할려면 필수 코드

API = "http://www.mois.go.kr/gpms/view/jsp/rss/rss.jsp"

#여기랑
values = {
    'ctxCd': '1012' #여기만 바꾸면 api 따옴
}
print('before',values)
params = urlencode(values)
print('after',params)

url = API + "?" + params
print("요청 url", url)

reqData = req.urlopen(url).read().decode('utf-8')
print("출력",reqData)
