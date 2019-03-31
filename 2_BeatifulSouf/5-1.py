#urljoin
from urllib.parse import urljoin #절대경로 파싱
baseUrl = "http://test.com/html/a.html" #test닷컴 경로에 html파일이 있다고 가정
print(">>", urljoin(baseUrl, "b.html")) #베이스유알엘에 b.html을 조인해라
print(">>", urljoin(baseUrl, "sub/b.html"))
print(">>", urljoin(baseUrl, "../index.html"))#..위로올라가자
print(">>", urljoin(baseUrl, "../img/img.jpg"))
print(">>", urljoin(baseUrl, "../css/img.css"))
