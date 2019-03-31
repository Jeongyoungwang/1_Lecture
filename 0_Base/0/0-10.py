#튜플
#immutable(값 바꿀 수 없음 ex 문자열) mutable(값변경 가능 ex 리스트)


import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')#아톰에서 한글 출력 할려면 필수 코드

my_tuple = ()
print(my_tuple)

print(type(my_tuple))


my_tuple = 1, 2, 3
print(my_tuple)

print(type(my_tuple))

#패킹과 언팩킹

my_tuple = 1, 2, 3 #패킹
print(my_tuple)


num1, num2, num3 = my_tuple
print(num1)
print(num2)
print(num3)

num1, num2 = num2, num1
print(num1)

print(num2)
