#자료형 변환

import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')#아톰에서 한글 출력 할려면 필수 코드


my_int = 1

print(type(my_int))

print(float(my_int))



print(str(my_int))
print(type(str(my_int)))

print(list(str(my_int)))
