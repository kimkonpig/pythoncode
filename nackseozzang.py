# 새싹이다
print('         ,r\'\"7')
print('r`-_   ,\'  ,/')
print(' \\. \". L_r\'')
print('   `~\\/')
print('      |')
print('      |')

import sys

H, M = map(int, input().split()) # 알람시간 H시 M분

if M < 45:
    if H == 0:
        H = 23
        M += 60
    else:
        H -= 1
        M += 60

print(H, M-45)