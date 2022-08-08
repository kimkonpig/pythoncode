T = int(input())

total_rst = []
for i in range(T):
    strOX = input()

    cnt = 0
    rst = []
    for j in range(len(strOX)):
        if strOX[j] == 'O':
            cnt += 1
            rst.append(cnt)            
        else:
            cnt = 0
    
    total_rst.append(sum(rst))

for i in total_rst:
    print(i)
