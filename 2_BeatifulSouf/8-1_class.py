#클래스 이미지는 스킵함

#클래스 생성자
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

class UserInfo: #사용자의 정보를 담는 클래스 선언
    def set_info(self, name, phone): #정보는 이름과 전화만,
        self.name = name #메소드 : 왼쪽, 오른쪽, 후진, 브레이크
        self.phone = phone

    def print_info(self): #정보를 출력해주는 함수 생성
        print("---------------")
        print("Name: " + self.name)
        print("Phone: " + self.phone)
        print("---------------") #붕어빵을 만드는 틀

user1 = UserInfo() #유저 정보를 담는 변수
user2 = UserInfo()
user3 = UserInfo()
user4 = UserInfo()


print(id(user1))
print(id(user2))

user1.set_info("kim","010-3433-7777")
user2.set_info("park","010-7777-2245")
user3.set_info("Jeong","010-4122-2233")
user4.set_info("Kwak","010-2334-4111")


user1.print_info() #클래스 출력
user2.print_info()
user3.print_info()
user4.print_info()


print(user1.__dict__) #인스턴스시킨 user1,2의 네임스페이스 확인 가능
print(user2.__dict__)

print(user1.phone,user1.name)
