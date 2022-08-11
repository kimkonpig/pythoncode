cnt = 0
T = int(input())

for case in range(T):
    str = input()
    flag = False

    for i in range(0, len(str)-1):
        for j in range(i+1, len(str)-1):
            if str[i] == str[j+1]:
                flag = True

    if flag == False:
        cnt += 1
    
print(cnt)