#포맷팅 -c언어스럼

import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')#아톰에서 한글 출력 할려면 필수 코드

my_str = 'My name is %s' % 'Young Choi'

print(my_str)


'%d %d' % (1, 2)

print('%d %d' % (1, 2))

'%f' % 3.14


print('%f' % 3.14)

#format -파이썬 같음


'My name is %s' % '조희진'

print('My name is %s' % '조희진')


'My name is {}'.format('조희진')

print('My name is {}'.format('조희진'))


'{} x {} = {}'.format(2, 3, 2*3)

print('{} x {} = {}'.format(2, 3, 2*3))



'{1} x {0} = {2}'.format(2, 3, 2*3)
print('{1} x {0} = {2}'.format(2, 3, 2*3))
