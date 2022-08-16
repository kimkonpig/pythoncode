cnt = 0
T = int(input())

for case in range(T):
    str = input()
    flag = False

    for i in range(0, len(str)-1):
            if str[i] == str[i+1]:
                pass
            elif str[i] in str[i+1:]:
                flag = True
                break

    if flag == False:
        cnt += 1
    
print(cnt)



# T = int(input())
# result = T

# for case in range(T):
#     str = input()

#     for i in range(0, len(str)-1):
#         if str[i] == str[i+1]:
#             pass
#         elif str[i] in str[i+1:]:
#             result -= 1
#             break
    
# print(result)
