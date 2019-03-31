#리스트

import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')#아톰에서 한글 출력 할려면 필수 코드


my_list = []

my_list = [1, 2, 3]

print(my_list)

students = ['덕수', '덕현', '소영']

for std in students:
    print(std)


#import random  #제비뽑기
#print(random.choice(students))


students.append('신영')

print(students)

students.append('봉란')

print(students)


students[0] = '영자'

print(students)



#my_tuple = ('영자', '신영', '덕수')
#print(my_tuple)
#my_tuple[0] = '봉란'
#print(my_tuple)


my_dict = {'헤흐': '남', 'Meta':'여'}
print(my_dict['헤흐'])
