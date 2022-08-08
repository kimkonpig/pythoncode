# # S = list(input())

# # 중복처리 / 아 중복처리하면 문자열 길이가 달라져서 틀림
# new_S = []
# for value in S:
#     if value not in new_S:
#         new_S.append(value)


# # 파이썬의 find() 함수를 사용하면 첫번째 위치를 리턴받을 수 있다!
S = input()
alphabet = list(range(ord('a'), ord('z')+1)) # a to z 아스키코드

for a in alphabet:
    print(S.find(chr(a)), end=' ')

# 1 0 -1 -1 2 -1 -1 -1 -1 4 3 -1 -1 7 5 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
# 1 0 -1 -1 2 -1 -1 -1 -1 4 3 -1 -1 7 5 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 
# 1 0 -1 -1 2 -1 -1 -1 -1 4 3 -1 -1 7 5 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1