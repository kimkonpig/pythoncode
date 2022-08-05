import sys

N = int(input())
origin_N = N
cnt = 0

while True:
    cnt += 1
    N_right = N%10
    total = N//10 + N%10

    new_N = int(str(N_right) + str(total%10))
    N = new_N
    if origin_N == new_N:
        break

print(cnt)

