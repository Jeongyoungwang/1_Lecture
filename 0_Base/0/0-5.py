#문자열

import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')#아톰에서 한글 출력 할려면 필수 코드

my_str = "김씨가족"

print(my_str)

print(type(my_str))

my_str = 'JW호박 Pumkin'

print(my_str)

print(type(my_str))


my_str = """제스퍼
토미
메타
"""
print(my_str) #큰따옴표 세개 작은따옴표도 줄세게
print(my_str) #큰따옴표 세개 작은따옴표도 줄세게
