import sys
import io
import requests
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#Response 상태코드
s = requests.Session()
r = s.get('http://httpbin.org/get')
#print(r.status_code)
#print(r.ok)

#https://jsonplaceholder.typicode.com

r = s.get('https://jsonplaceholder.typicode.com/posts/1')
#print(r.text)
print(r.json())
print(r.json().keys())
print(r.json().values()) #키값 제외하고, 벨류값만 출력
print(r.encoding) #한글 깨지는거 방지 진짜 중요
print(r.content) #바이너리 형태의 데이터로 가져옴
print(r.raw) #로우 형태의 데이터로 가져옴
