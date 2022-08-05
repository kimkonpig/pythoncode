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

while(True):
    try:
        A, B = sys.stdin.readline().rstrip().split()
        print(int(A)+int(B))
    except:
        break