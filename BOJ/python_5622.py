num_list = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

s = list(input())
time = 0

for i in s:
    for num in num_list:
        if i in num:
            time += 2 + num_list.index(num) + 1 # 기본 2초에 인덱스 + 1만큼 추가해야함

print(time)