#1.클래스생성자 이해하기
import sys
import io
import requests
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

class UserInfo:  #클래스 선언 클래스 이름 사용자 정보를 담는 UserInfo
    def set_info(self, name, phone): #정보는 2가지 이름과 전화번호, 일단 메소드만 작성
        self.name = name #메소드1, 유저인포 자체 name 변수에는 name 저장
        self.phone = phone  #메소드2 phone 변수에는 phone

    def print_info(self):
        print("-----------")
        print("Name: " + self.name)
        print("Phone: "+ self.phone)
        print("-----------")

user1 = UserInfo()   #인스턴스화 방금만든 클래스이름 적으면됨
user2 = UserInfo()

print(id(user1))
print(id(user2))

user1.set_info("kim","010-3433-7777")
user2.set_info("park","010-3113-1133")

user1.print_info()
user2.print_info()

print(user1.__dict__)
print(user2.__dict__)

print(user1.phone,user1.name)
