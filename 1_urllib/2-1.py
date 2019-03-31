#아톰에서 한글 출력 할려면 필수 코드
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


#urlretrieve

import urllib.request as dw

imgUrl ="https://t1.daumcdn.net/thumb/R1280x0/?fname=http://t1.daumcdn.net/brunch/service/guest/image/auhSRNEa-p9c6XMgziO_7D0W1sk.png"
htmlURL ="http://google.com"

savePath1 ="c:/test1.jpg"
savePath2 ="c:/index.html"

dw.urlretrieve(imgUrl, savePath1)
dw.urlretrieve(htmlURL, savePath2)

print("다운로드 완료!")
