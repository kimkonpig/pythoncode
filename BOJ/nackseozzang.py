# 새싹이다
print('         ,r\'\"7')
print('r`-_   ,\'  ,/')
print(' \\. \". L_r\'')
print('   `~\\/')
print('      |')
print('      |')

# input().split()
# sys.stdin.readline().rstrip().split()

import sys

N = int(input())
origin_N = N
cnt = 0
flag = True

while flag:
    cnt += 1

    N_right = N%10

    if N < 10:
        total = N
    else:
        total = N//10 + N%10

    new_N = str(N_right) + str(total%10)

    if origin_N == int(new_N):
        print(cnt)
        break
    else:
        N = int(new_N)