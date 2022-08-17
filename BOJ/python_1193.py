# 1 : 1/1 (0, 0)
# 2 : 1/2 (0, 1)
# 3 : 2/1 (1, 0)
# 4 : 3/1 (2, 0)
# 5 : 2/2 (1, 1)
# 6 : 1/3 (0, 2)
# 7 : 1/4
# 8 : 2/3
# 9 : 3/2
# ...
# 14 : 2/4
# 사선 짝수라인은 작은수부터
# 사선 홀수라인은 큰수부터


input_num = int(input())
line = 0 # 라인 넘버
max_num = 0 # 라인에서 가장 큰 수

while input_num > max_num:
    line += 1
    max_num += 1

gap = max_num - input_num

if line % 2 == 0: # 짝수 라인
    
else: # 홀수 라인
