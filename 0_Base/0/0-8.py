#문자열 인덱싱

import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')#아톰에서 한글 출력 할려면 필수 코드


a = 'python'

print(a[0])

my_name = "김왼손의 왼손코딩"

print(my_name[3])


print(my_name[8])

print(my_name[-1])

#문자열 슬라이싱 (치즈를 써는거)

a = 'python'

print(a[0:2])


print(a[:2])

#문자열 메서드

print(my_name.split())


fruit_str = '거봉 수박 포도 복숭아 백도 망고 딸기 배 참외 찹쌀떡'
print(fruit_str)

fruits = fruit_str.split()
print(fruits)

#독스트링-문자열 주석으로 씀 ?? 함수배울 때 ㄱ

#이것이 주석입니다.
"""이것도 주석입니다."""

print()

#end

print('집단지성')
print('집단지성', end='/')
print('집단지성', end='미운코딩새끼')


#이스케이프 \n \t 원화표시=백스페이스

print('미운코딩새끼의 집단지성들')

print('미운코딩새끼의\n집단지성들')

print('미운코딩새끼의\t집단\n지성들')

print('미운', end='\t')

print('미운', end='\t'); print('코딩')
