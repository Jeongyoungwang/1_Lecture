import sys
import io
import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

imgUrl ="http://post.phinf.naver.net/20150527_274/whtjdgus1666_1432689219314TApr5_JPEG/mug_obj_143268921826930359.jpg"
htmlURL = "http://google.com"

savePath1 ="C:/Users/LG/Downloads/test1.jpg"
savePath2 ="C:/Users/LG/Downloads/index.html"

dw.urlretrieve(imgUrl, savePath1)
dw.urlretrieve(htmlURL, savePath2)

print("다운로드 완료!")
