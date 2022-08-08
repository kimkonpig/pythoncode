def check(n):
    hansu_cnt = 0
    for i in range(1, n+1):
        lst = list(map(int, str(i)))
        if i < 100:
            hansu_cnt += 1
        elif lst[0]-lst[1] == lst[1]-lst[2]:
            hansu_cnt += 1
    return hansu_cnt

N = int(input())
print(check(N))