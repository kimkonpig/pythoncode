C = int(input())

rst = []
for i in range(C):
    score_list = list(map(int, input().split()))

    total_cnt = score_list[0]
    score_list = score_list[1:]

    score_avg = sum(score_list) / total_cnt # 평균
    
    # 평균 넘는 학생 수
    pass_cnt = 0
    for j in score_list:
        if j > score_avg:
            pass_cnt += 1

    # 평균 넘는 학생 비율 
    rst.append(pass_cnt / total_cnt * 100)

for i in rst:
    print('{:.3f}%'.format(i)) # 반올림하여 소수점 셋째 자리까지 출력