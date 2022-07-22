## 숫자 자료형
print(5) # 양수
print(-10) # 음수
print(3.14) # 실수
print(1000)
print(5+3) # 덧셈
print(2*8) # 곱셈
print(3*(3+1)) # 우선순위 연산

## 문자열 자료형
print('풍선')
print("나비")
print("ㅋㅋㅋㅋㅋㅋㅋㅋ")
print("ㅋ"*9)

## boolean 자료형
## 참/거짓
print(5 > 10)
print(5 < 10)
print(True)
print(False)
print(not True)
print(not False)
print(not (5 > 10))

## 변수
## 애완동물을 소개해주세요.
animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age >= 3

print("우리집 " + animal + "의 이름은 " + name + "예요")
hobby = "공놀이"
# print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요") # '+'로 문자열 붙일때는 str(age)
print(name, "는 ", age, "살이며, ", hobby, "을 아주 좋아해요") # ','로 문자열 붙일때는 age 사용 가능, ',' 사용하면 빈칸이 하나 들어간다
print(name + "는 어른일까요? " + str(is_adult))

################################################################################

## 연산자
print(1+1) # 2
print(3-2) # 1
print(5*2) # 10
print(6/3) # 2

print(2**3) # 8
print(5%3) # 나머지 구하기 2
print(10%3) # 1
print(5//3) # 몫 구하기 1
print(10//3) # 3

## 비교연산
print(10 > 3) # True
print(4 >= 7) # False
print(10 < 3) # False
print(5 <= 5) # True

print(3 == 3) # True
print(4 == 2) # False
print(3+4 == 7) # True

print(1 != 3) # True
print(not(1 != 3)) # False

print((3 > 0) and (3 < 5)) # True
print((3 > 0) & (3 < 5)) # True

print((3 > 0) or (3 > 5)) # True
print((3 > 0) | (3 > 5)) # True

print((5 > 4 > 3)) # True
print((5 > 4 > 7)) # False

## 간단한 수식
print(2 + 3 * 4) # 14
print((2 + 3) * 4) # 20

number = 2 + 3 * 4 # 14
print(number)
number = number + 2 # 16
print(number)
number += 2 # 18
print(number)
number *= 2 # 36
print(number)
number /= 2 # 18
print(number)
number -= 2 # 16
print(number)

number %= 5 # 1
print(number)

## 숫자 처리 함수
print(abs(-5)) # -5에 대한 절대값 = 5
print(pow(4, 2)) # 4의 2승 = 4^2 = 4*4 = 16
print(max(5, 12)) # 최대값 = 12
print(min(5, 12)) # 최소값 = 5
print(round(3.14)) # 반올림 = 3
print(round(4.99)) # 반올림 = 5

from math import * # math 라이브러리 안에 있는 모든 모듈 import
print(floor(4.99)) # 내림 = 4
print(ceil(3.14)) # 올림 = 4
print(sqrt(16)) # 16의 제곱근 = 4


## 랜덤 함수
from random import * # random 라이브러리 안에 있는 모든 모듈 import
print(random()) # 0.0 이상 1.0 미만의 임의의 값 생성
print(random() * 10) # 0.0 이상 10.0 미만의 임의의 값 생성
print(int(random() * 10)) # 0 이상 10 미만의 임의의 값 생성
print(int(random() * 10)) # 0 이상 10 미만의 임의의 값 생성
print(int(random() * 10)) # 0 이상 10 미만의 임의의 값 생성
print(int(random() * 10) + 1) # 1 이상 10 이하의 임의의 값 생성
print(int(random() * 10) + 1) # 1 이상 10 이하의 임의의 값 생성
print(int(random() * 10) + 1) # 1 이상 10 이하의 임의의 값 생성
print(int(random() * 10) + 1) # 1 이상 10 이하의 임의의 값 생성
print(int(random() * 10) + 1) # 1 이상 10 이하의 임의의 값 생성
print(int(random() * 10) + 1) # 1 이상 10 이하의 임의의 값 생성

print(int(random() * 45) + 1) # random()+1 - 1 이상 45 이하의 임의의 값 생성 - 로또
print(int(random() * 45) + 1) # random()+1 - 1 이상 45 이하의 임의의 값 생성 - 로또
print(int(random() * 45) + 1) # random()+1 - 1 이상 45 이하의 임의의 값 생성 - 로또
print(int(random() * 45) + 1) # random()+1 - 1 이상 45 이하의 임의의 값 생성 - 로또
print(int(random() * 45) + 1) # random()+1 - 1 이상 45 이하의 임의의 값 생성 - 로또
print(int(random() * 45) + 1) # random()+1 - 1 이상 45 이하의 임의의 값 생성 - 로또

print(randrange(1, 46)) # randrange() - 1 이상 45 이하의 임의의 값 생성 - 로또
print(randrange(1, 46)) # randrange() - 1 이상 45 이하의 임의의 값 생성 - 로또
print(randrange(1, 46)) # randrange() - 1 이상 45 이하의 임의의 값 생성 - 로또
print(randrange(1, 46)) # randrange() - 1 이상 45 이하의 임의의 값 생성 - 로또
print(randrange(1, 46)) # randrange() - 1 이상 45 이하의 임의의 값 생성 - 로또
print(randrange(1, 46)) # randrange() - 1 이상 45 이하의 임의의 값 생성 - 로또

print(randint(1, 45)) # randint() - 1 이상 45 이하의 임의의 값 생성

################################################################################

## 문자열
sentence = '나는 소녀입니다'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = """
나는 소년이고,
파이썬은 쉬워요
"""
print(sentence3)

## 슬라이싱
jumin = "931009-1234567"
print("성별 : " + jumin[7])
print("연 : " + jumin[0:2]) # 0부터 2직전까지
print("월 : " + jumin[2:4]) # 2부터 4직전까지
print("일 : " + jumin[4:6]) # 4부터 6직전까지
print("생년월일 : " + jumin[:6]) # 처음부터 6직전까지
print("뒤 7자리 : " + jumin[7:]) # 7부터 끝까지
print("뒤 7자리 (뒤에부터) : " + jumin[-7:]) # 맨 뒤(-1)에서 7번째부터 끝까지

## 문자열 처리 함수
python = "Python is Amazing"
print(python.lower()) # 모든 문자를 소문자로
print(python.upper()) # 모든 문자를 대문자로
print(python[0].isupper()) # 0번째 문자가 대문자인지 확인
print(len(python)) # 문자열 길이
print(python.replace("Python", "Java"))

index = python.index("n")
print(index)
index = python.index("n", index + 1) # 처음 index=5 이후부터 찾기 시작
print(index)

print(python.find("Java")) # find() : 찾는 값이 없으면 -1 반환
# print(python.index("Java")) # index() : 찾는 값이 없으면 에러

print(python.count("n"))


## 문자열 포맷
# 방법 1 : %
print("나는 %d살입니다." % 20) # %d : 정수
print("나는 %s을 좋아해요." % "파이썬") # %s : 문자열
print("Apple 은 %c로 시작해요" % "A") # %c : 문자
print("나는 %s살입니다." % 20) # %s : 정수도 가능
print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간")) # 두개의 값

# 방법2 : {} + format
print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아해요.".format("노랑", "검정"))
print("나는 {1}색과 {0}색을 좋아해요.".format("노랑", "검정"))

# 방법3 : {} + format + 변수
print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color = "빨간"))
print("나는 {age}살이며, {color}색을 좋아해요.".format(color = "빨간", age = 20))

# 방법4 (python v3.6 이상부터 가능) : 변수 + f"{}"
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")

## 탈출문자
print("백문이 불여일견 \n백견이 불여일타") # \n : 줄바꿈
print('저는 "나도코딩"입니다.')
print("저는 \"나도코딩\"입니다.") # \" : 문장 내에서 큰따옴표 쓸 때
print("D:\\Steam\\music") # \\ : 문장 내에서 \ 쓸 때
print("Red Apple \rPine ") # \r : 커서를 맨 앞으로 이동
print("Redd\b Apple") # \b : 백스페이스(한 글자 지움)
print("Red\tApple") # \t : 탭