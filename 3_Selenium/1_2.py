#2.
import sys
import io
import requests
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

class UserInfo:  #클래스 선언 클래스 이름
    def __init__(self, name, phone): #객체의 초기화 이니셜라이즈
        self.name = name #메소드1
        self.phone = phone  #메소드2

    def print_info(self):
        print("-----------")
        print("Name: " + self.name)
        print("Phone: "+ self.phone)
        print("-----------")

    def __del__(self): #쓰레기 청소부
        print("delete!")

user1 = UserInfo("kim","010-3433-7777")   #인스턴스화
user2 = UserInfo("park","010-3113-1133")

print(id(user1))
print(id(user2))

#user1.set_info("kim","010-3433-7777")
#user2.set_info("park","010-3113-1133")

user1.print_info()
user2.print_info()
