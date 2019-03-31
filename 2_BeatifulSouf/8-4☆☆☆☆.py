#클래스 변수와 인스턴스 변수의 차이점

import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#클래스 변수, 인스턴스 변수 클래스 변수는 공유 인스턴스 변수는 안나와 그래도 접근은 가능

class Warehouse: #창고라는 클래스 선언
    stock_num = 0 #처음으로 변수 선언, 재고량=num
    def __init__(self, name): #생성자를 만들고, name만 받음
        self.name = name
        Warehouse.stock_num += 1

    def __del__(self):
        Warehouse.stock_num -= 1

user1 = Warehouse('kim')
user2 = Warehouse('park')

print(user1.name) #김과 박의 인스턴스 생성된거 확인가능
print(user2.name)

print("--------------------")
print("--------------------")
print(user1.__dict__) #user1 네임스페이스
print(user2.__dict__) #user2 네임스페이스
print(Warehouse.__dict__) #인스턴스 네임스페이스 -> 클래스 네임스페이스, 클래스 변수(공유)

print("---------")
print("---------")
print(user1.stock_num)
print(user2.stock_num)
