import sys
import io
import urllib.request as dw
#숙제1
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')#아톰에서 한글 출력 할려면 필수 코드

imgUrl ="https://ssl.pstatic.net/tveta/libs/1190/1190118/5c7b4d395a9764330547_20180326134325007.jpg"

savePath1 ="c:/숙제1.jpg"

f = dw.urlopen(imgUrl).read()

with open(savePath1, 'wb') as saveFile2:
    saveFile2.write(f)


#옛날 코드
#saveFile1 = open(savePath1, 'wb') # w: write, r:read, a:add
#saveFile1.write(f)
#saveFile1.close()

print("다운로드 완료!")
