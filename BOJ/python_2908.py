# A, B = map(list, input().split())
# A.reverse()
# B.reverse()

# rst_A = rst_B = ''
# for i in A: rst_A += i
# for i in B: rst_B += i

# print(max(rst_A, rst_B))


# # 대박 짧게 가능..
# # https://blog.wonkyunglee.io/3

A, B = input().split()
A = A[::-1] # 처음부터 끝까지 역순으로
B = B[::-1]

print(max(A, B))