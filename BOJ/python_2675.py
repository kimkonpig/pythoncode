T = int(input())

for i in range(T):
    R, S = input().split() # R : 반복횟수, S = 문자열
    for j in S:
        print(int(R) * j, end='')
    print()


    # rst = []
    
    # S = list(S)

    # for k in range(len(S)):
    #     for j in range(int(R)):
    #         rst.append(S[k])

    # result = ''
    # for a in rst:
    #     result += a
    
    # print(result)