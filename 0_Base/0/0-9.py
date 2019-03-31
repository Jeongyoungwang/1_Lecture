#리스트

#immutable(값 바꿀 수 없음 ex 문자열) mutable(값변경 가능 ex 리스트)


import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')#아톰에서 한글 출력 할려면 필수 코드


my_list = [] #빈 리스트

print(my_list)

print(type(my_list))

my_list = [1, 2, 3]

print(my_list)

std = ['이에스', '이에스2']

print(std)


#리스트 값 추가하기

std.append('토미')

print(std)

std.append('찹쌀떡')

print(std)

animals = []

animals.append('코알라')

print(animals)

animals.append('바다소')

print(animals)

#humans.append('조희진')

#print(animals)

humans = []

humans.append('조희진')

print(humans)

#리스트 인덱싱, 슬라이싱

print(animals)
humans.append('조희진')

print(animals)

animals.append('아나콘다')

animals.append('바다코끼리')

animals.append('고래')

print(animals)

print(animals[0])

print(animals[0:3])

print(animals[:3])

#메소드
print(animals)

animals.sort()

print(animals)

print(animals.count('바다소'))

print(len(animals))
