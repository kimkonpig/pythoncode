# Quiz6) 표준 체중을 구하는 프로그램을 작성하시오.
# * 표준 체중 : 각 개인의 키에 적당한 체중

# (성별에 따른 공식)
# 남자 : 키(m) x 키(m) x 22
# 여자 : 키(m) x 키(m) x 21

# 조건1 : 표준 체중은 별도의 함수 내에서 계산
#         * 함수명 : std_weight
#         * 전달값 : 키(height), 성별(gender)
# 조건2 : 표준 체중은 소수점 둘째자리까지 표시

# (출력 예제)
# 키 175cm 남자의 표준 체중은 67.38kg 입니다.

def std_weight(height, gender): # 키 m 단위 (실수), 성별 "남자"/"여자"
    height *= 0.01
    if gender == "여자":
        weight = height * height * 21
    else:
        weight = height * height * 22
    return round(weight, 2)

# height = 175
# gender = "남자"
height = int(input("키 입력 : "))
gender = input("성별 입력 : ")
weight = std_weight(height, gender)
print("키 {0} {1}의 표준 체중은 {2} 입니다.".format(height, gender, weight))

