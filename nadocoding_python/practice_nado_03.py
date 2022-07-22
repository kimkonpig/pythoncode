## 분기문
# weather = "맑음"
weather = input("오늘 날씨는 어때요? ") # 사용자 입력
if weather == "비" or weather == "눈":
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("준비물이 필요 없습니다.")

temp = int(input("기온은 어때요? ")) # 사용자가 입력한 값을 int형으로 변환
if 30 <= temp:
    print("너무 더워요. 나가지 마세요.")
elif 10<= temp and temp < 30:
    print("괜찮은 날씨에요.")
elif 0 <= temp < 10:
    print("외투를 챙기세요.")
else:
    print("너무 추워요. 나가지 마세요.")

################################################################################

## 반복문
print("대기번호 : 1")
print("대기번호 : 2")
print("대기번호 : 3")
print("대기번호 : 4")

for waiting_no in range(1, 6): # 1부터 5까지
    print("대기번호 : {0}".format(waiting_no))

starbucks = ["아이언맨", "토르", "아이엠 그루트"]
for customer in starbucks:
    print("{0}, 커피가 준비되었습니다.".format(customer))


customer = "토르"
index = 5
while index >= 1:
    print("{0}, 커피가 준비되었습니다. {1} 번 남았어요".format(customer, index))
    index -= 1
    if index == 0:
        print("커피는 폐기처분되었습니다.")


customer = "아이언맨"
index = 0
while True: # 무한루프
    print("{0}, 커피가 준비되었습니다. 호출 {1} 회".format(customer, index))
    index += 1


customer = "토르"
person = "Unknown"

while person != customer:
    print("{0}, 커피가 준비되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요? ")


## continue, break
absent = [2, 5] # 결석
no_book = [7] # 책을 안가져왔음
for student in range(1, 11): # 출석번호 1부터 10
    if student in absent: # 결석한 학생이라면 continue
        continue
    elif student in no_book: # 책을 안가져온 학생이라면 break, for문 종료
        print("오늘 수업 여기까지. {0}은 교무실로 따라와".format(student))
        break
    print("{0}, 책을 읽어봐".format(student))


## 한줄 for
# 출석번호가 1, 2, 3, 4가 있는데 앞에 100을 붙이기로 함 -> 101, 102, 103, 104
students = [1, 2, 3, 4, 5]
print(students)
students = [i+100 for i in students]
print(students)

# 학생 이름을 길이로 변환
students = ["Iron man", "Thor", "I am groot"]
print(students)
students = [len(i) for i in students]
print(students)

# 학생 이름을 대문자로 변환
students = ["Iron man", "Thor", "I am groot"]
print(students)
students = [i.upper() for i in students]
print(students) 