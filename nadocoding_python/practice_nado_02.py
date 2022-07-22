## 리스트 []
# 지하철 칸 별로 10명, 20명, 30명
subway = [10, 20, 30]
print(subway)

subway = ["유림", "윤기", "삐순"]
print(subway)

# 윤기가 몇 번째 칸에 타고 있는가?
print(subway.index("윤기")) # 1

# 민성이가 다음 정류장에서 다음 칸에 탐
subway.append("민성")
print(subway)

# 김허저비가 윤기와 삐순 사이에 탐
subway.insert(2, "김저비")
print(subway)

# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
print(subway.pop())
print(subway)
# print(subway.pop())
# print(subway)
# print(subway.pop())
# print(subway)

# 같은 이름의 사람이 몇 명 있는지 확인
subway.append("유림")
print(subway)
print(subway.count("유림")) # 2

# 정렬
num_list = [5,2,4,3,1]
num_list.sort()
print(num_list) # 1,2,3,4,5

# 순서 뒤집기
num_list.reverse()
print(num_list) # 5,4,3,2,1

# 모두 지우기
num_list.clear()
print(num_list)

# 다양한 자료형 함께 사용 가능
mix_list = ["삐순", 20, True]
print(mix_list)

# 리스트 확장
num_list = [5,2,4,3,1]
mix_list = ["삐순", 20, True]
num_list.extend(mix_list)
print(num_list)


## 사전
cabinet = {3:"유림", 100:"삐순"} # {key:value, key:value, ...}
print(cabinet[3]) # 유림
print(cabinet[100]) # 삐순
print(cabinet.get(3)) # 유림
print(cabinet.get(5)) # None
print(cabinet.get(5, "사용 가능")) # 사용 가능
print(cabinet[5]) # 에러 떨어짐
print(3 in cabinet) # True
print(5 in cabinet) # False

cabinet = {"A-3":"윤기", "B-100":"허저비"} # {key:value, key:value, ...}
print(cabinet["A-3"])
print(cabinet["B-100"])

# 새 손님
cabinet = {"A-3":"윤기", "B-100":"허저비"} # {key:value, key:value, ...}
cabinet["C-20"] = "민성"
cabinet["A-3"] = "콩픽"
print(cabinet)

# 간 손님
del cabinet["A-3"]
print(cabinet)

# key들만 출력
print(cabinet.keys())

# value들만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

# 목욕탕 폐점
cabinet.clear()
print(cabinet)


# 튜플 : 내용 변경이나 추가 불가, 속도가 리스트보다 빠름
menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])
# menu.add("생선까스") # 에러남, 튜플은 추가 불가

# name = "삐순"
# age = 19
# hobby = "잠자기"
# print(name, age, hobby)
# 위 내용을 튜플 형태로 변환
(name, age, hobby) = ("삐순", 19, "잠자기")
print(name, age, hobby)


# 집합(set) : 중복 안됨, 순서 없음
my_set = {1,2,3,3,3}
print(my_set) # 1,2,3

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# 교집합 (java와 python을 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python))

# 합집합 (java도 할 수 있거나 python도 할 수 있는 개발자)
print(java | python)
print(java.union(python))

# 차집합 (java는 할 줄 알지만 python을 할 줄 모르는 개발자)
print(java - python)
print(java.difference(python))

# python을 할 줄 아는 사람이 늘어남
python.add("김태호")
print(python)

# java을 잊어버린 개발자
java.remove("김태호")
print(java)


## 자료구조의 변경
# 커피숍
menu = {"커피", "우유", "주스"}
print(menu, type(menu)) # type() : class 'set', {}

menu = list(menu)
print(menu, type(menu)) # type() : class 'list', []

menu = tuple(menu)
print(menu, type(menu)) # type() : class 'tuple', ()

menu = set(menu)
print(menu, type(menu)) # type() : class 'set', {}
