# ## 함수
# def open_account():
#     print("새로운 계좌가 생성되었습니다.")

# # open_account()

# ## 전달값과 반환값
# def deopsit(balance, money): # 입금
#     print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance + money))
#     return balance + money

# def withdraw(balance, money): # 출금
#     if balance >= money: # 잔액이 출금보다 많으면
#         print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance - money))
#         return balance - money
#     else:
#         print("출금이 완료되지 않았습니다. 잔액은 {0} 원입니다.".format(balance))
#         return balance

# def withdraw_night(balance, money): # 저녁에 출금
#     commission = 100 # 수수료
#     return commission, balance - money - commission # 튜플형식

# balance = 0 # 잔액
# balance = deopsit(balance, 1000) # 1000원 입금
# # balance = withdraw(balance, 2000) # 2000원 출금시도
# # balance = withdraw(balance, 500) # 500원 출금시도
# commission, balance = withdraw_night(balance, 500)
# print("수수료 {0} 원이며, 잔액은 {1} 원입니다.".format(commission, balance))

################################################################################

# ## 기본값
# # def profile(name, age, main_lang):
# #     print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}" \
# #         .format(name, age, main_lang))

# # profile("유림", 20, "파이썬")
# # profile("윤기", 25, "자바")

# # 같은 학교, 같은 학년, 같은 반, 같은 수업
# # 기본값 설정 : 함수 호출 시 값이 없으면 함수에 설정되어있는 기본값 사용
# def profile(name, age=17, main_lang="파이썬"):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}" \
#         .format(name, age, main_lang))

# profile("유림") # 이름 : 유림     나이 : 17       주 사용 언어 : 파이썬
# profile("윤기") # 이름 : 윤기     나이 : 17       주 사용 언어 : 파이썬

################################################################################
# ## 키워드
# def profile(name, age, main_lang):
#     print(name, age, main_lang)

# profile(name="유림", main_lang="파이썬", age=20)
# profile(main_lang="자바", age=25, name="윤기")

################################################################################
## 가변 인자 : *을 사용한 변수
# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ") # end=" " : print후 줄바꿈을 하지 않는다.
#     print(lang1, lang2, lang3, lang4, lang5)

# profile("유림", 20, "python", "java", "c", "c++", "c#")
# profile("윤기", 25, "kotlin", "swift", "", "", "")


# def profile(name, age, *language):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ") # end=" " : print후 줄바꿈을 하지 않는다.
#     for lang in language:
#         print(lang, end=" ")
#     print()

# profile("유림", 20, "python", "java", "c", "c++", "c#", "javascript")
# profile("윤기", 25, "kotlin", "swift")

################################################################################
## 지역변수와 전역변수
# gun = 10

# def checkpoint(soldiers): # 경계근무
#     # gun = 20 # 지역변수
#     global gun # 전역 공간에 있는 gun 사용
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))

# def checkpoint_ret(gun, soldiers):
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))
#     return gun

# print("전체 총 : {0}".format(gun))
# # checkpoint(2) # 2명이 경계근무를 나감
# gun = checkpoint_ret(gun, 2)
# print("남은 총 : {0}".format(gun))

################################################################################
## 표준 입출력
# print("Python", "Java", "JavaScript", sep=" vs ") # Python vs Java vs JavaScript
# print("Python", "Java", "JavaScript", sep=",", end="?") # 문장의 끝에 ? 추가
# print("무엇이 더 재밌을까요?")

# import sys
# print("Python", "Java", file=sys.stdout) # 표준 출력
# print("Python", "Java", file=sys.stderr) # 표준 에러

## 시험 성적
# scores = {"수학":0, "영어":50, "코딩":100}
# for subject, score in scores.items():
#     # print(subject, score)
#     print(subject.ljust(8), str(score).rjust(4), sep=":") # ljust : 왼쪽정렬/8칸확보, rjust : 오른쪽정렬/4칸확보

# # 은행 대기순번표
# # 001, 002, 003 ...
# for num in range(1, 21):
#     print("대기번호 : " + str(num).zfill(3)) # zfill : 3칸 확보, 값이 없는 빈공간은 0으로 채움

# answer = input("아무 값이나 입력하세요 : ") # input은 항상 type = str 형태로 저장됨
# # answer = 10
# # print(type(answer))
# print("입력하신 값은 " + answer + "입니다.")

################################################################################
## 다양한 출력 포맷

# 빈 자리는 빈공간으로 두고(' '), 오른쪽 정렬을 하되('>'), 총 10자리 공간을 확보('10')
print("{0: >10}".format(500)) # '       500'

# 양수일 땐 +로 표시, 음수일 땐 -로 표시
print("{0: >+10}".format(500)) # '      +500'
print("{0: >+10}".format(-500)) # '      -500'

# 왼쪽 정렬('<')하고, 빈칸을 _로 채움('_')
print("{0:_<10}".format(500)) # '500_______'

# 3자리마다 콤마를 찍어주기
print("{0:,}".format(10000000000)) # '10,000,000,000'

# 3자리마다 콤마를 찍고 +- 부호 붙이기
print("{0:+,}".format(10000000000)) # '+10,000,000,000'
print("{0:+,}".format(-10000000000)) # '-10,000,000,000'

# 3자리마다 콤마를 찍어주기, 부호도 붙이고, 30 자릿수 확보하기, 왼쪽 정렬
# 돈이 많으면 행복하니까 빈 자리는 ^ 로 채워주기
print("{0:^<+30,}".format(100000000000000)) # '+100,000,000,000,000^^^^^^^^^^'

# 소수점 출력
print("{0:f}".format(5/3)) # '1.666667'

# 소수점 특정 자리수까지만 표시(소수점 셋째 자리에서 반올림)
print("{0:.2f}".format(5/3)) # '1.67'