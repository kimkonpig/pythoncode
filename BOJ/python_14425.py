N, M = map(int, input().split())

S = set()
for i in range(N):
    S.add(input())

vali = []
for i in range(M):
    vali.append(input())

count = 0
for i in vali:
    if i in S:
        count += 1

print(count)