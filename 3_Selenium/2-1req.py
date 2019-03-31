import sys
import io
import requests
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

s = requests.Session()  #세션열림

#r = s.get('https://manage.searchad.naver.com/customers/1139044/tool/keyword-planner') #PUT(FETCH), DELETE, GET, POST
#print('1',r.text)


#r = s.get('http://httpbin.org/cookies',cookies={'from':'myName'}) #페이로드라함
#print(r.text)

url = 'http://httpbin.org/get'
headers = {'user-agent':'myPythonApp_1.0.0'}

#r = s.get(url,headers=headers)
#print(r.text)

s.close() #이걸 써야 자원 반납됨

with requests. Session() as s:
    r = s.get('https://www.naver.com')
    print(r.text)
