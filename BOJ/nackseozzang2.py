# 숫자야구
from random import randint

# 컴퓨터가 뽑은 숫자
def generate_computer_numbers():
    comp_nums = []
    for i in range(3):
        num = randint(0, 9)
        while num in comp_nums:
            num = randint(0, 9)
        comp_nums.append(num)

    print('0과 9 사이의 서로 다른 숫자 3개를 랜덤한 숫자로 뽑았습니다.')
    return comp_nums

# 0과 9 사이의 서로 다른 숫자인지 확인
def check_validation(list):
    for i in range(len(list)):
        if list[i] > 9 | list[i] < 0:
            print('범위를 벗어나는 숫자입니다. 다시 입력하세요.')
            return False
    for i in range(len(list)-1):
        if list[i] == list[i+1]:
            print('중복되는 숫자입니다. 다시 입력하세요.')
            return False
    return True

# 사용자가 숫자 뽑기
def set_numbers():
    num_list = []
    for i in range(1,4):
        num_list.append(int(input(str(i)+'번째 숫자를 입력하세요: ')))
        while check_validation(num_list) == False:
            num_list[len(num_list)-1] = int(input(str(i)+'번째 숫자를 입력하세요: '))
    return num_list

# 스트라이크, 볼 카운트
def check_strike_ball_cnt(origin_list, num_list):
    strike_cnt = ball_cnt = 0
    for i in range(len(num_list)):
        for j in range(len(origin_list)):
            if num_list[i] == origin_list[j]:
                if i == j:
                    strike_cnt += 1
                else:
                    ball_cnt += 1
    return strike_cnt, ball_cnt

# 메인 시작
origin_numbers = generate_computer_numbers()
print(origin_numbers)
print('숫자 3개를 하나씩 차례대로 입력하세요.')

game_cnt = 0
while True:
    game_cnt += 1
    number_list = set_numbers()

    s_cnt, b_cnt = check_strike_ball_cnt(origin_numbers, number_list)
    print('{0}S {1}B'.format(s_cnt, b_cnt))

    if s_cnt == 3:
        print('축하합니다. {0}번 만에 숫자 3개의 값과 위치를 모두 맞추셨습니다.'.format(game_cnt))
        break