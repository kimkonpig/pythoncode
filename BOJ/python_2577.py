import sys

total = 1
for i in range(0, 3):
    total *= int(input())

total = str(total)

for i in range(0, 10):
    cnt = 0
    for j in range(0, len(total)):
        if i == int(total[j]):
            cnt += 1
    print(cnt)

# 짧은 해답 개쩐다
# a = int(input())
# b = int(input())
# c = int(input())

# d = list(map(int, str(a*b*c)))

# for i in range(10):
#     print(d.count(i))