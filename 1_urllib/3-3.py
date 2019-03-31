import sys
import io
 #urlencode-ex)my ip api
from urllib.parse import urlencode

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')#아톰에서 한글 출력 할려면 필수 코드

#https://www.ipify.org/

API = "https://api.ipify.org" #변수선언

values = {
'format': 'jsonp' #딕셔너리 형태로
}
print('before',values)
params = urlencode(values)
print('after',params)

url = API + "?" + params
print("요청 url", url)

reqData = req.urlopen(url).read().decode('utf-8')
print("출력",reqData)
