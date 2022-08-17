N = int(input())
zip = cnt = 1

while N > zip:
    zip += 6 * cnt # 1 6 12 18 24 30
    cnt += 1

print(cnt)