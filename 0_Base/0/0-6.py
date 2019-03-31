#포맷팅

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
