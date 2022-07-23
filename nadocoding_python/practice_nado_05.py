# 파일 입출력
score_file = open("score.txt", "w", encoding="utf-8") # write
print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
score_file.close()

score_file = open("score.txt", "a", encoding="utf-8") # append
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100")
score_file.close()

score_file = open("score.txt", "r", encoding="utf-8") # read
print(score_file.read()) # 파일의 모든 내용 읽어오기
score_file.close()

score_file = open("score.txt", "r", encoding="utf-8")
print(score_file.readline(), end="") # 줄별로 읽기, 한줄 읽고 커서는 다음줄로 이동
print(score_file.readline(), end="")
print(score_file.readline(), end="")
print(score_file.readline(), end="")
score_file.close()

score_file = open("score.txt", "r", encoding="utf-8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line, end="") # 줄바꿈 없애기
score_file.close()

score_file = open("score.txt", "r", encoding="utf-8")
lines = score_file.readlines() # list 형태로 저장
for line in lines:
    print(line, end="")
score_file.close()

################################################################################
# pickle
import pickle
profile_file = open("profile.pickle", "wb") # pickle을 쓰려면 bynary 타입 필수
profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
print(profile)
pickle.dump(profile, profile_file) # profile에 있는 정보를 profile_file에 저장
profile_file.close()

import pickle
profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) # file에 있는 정보를 profile에 불러오기
print(profile)
profile_file.close()

################################################################################
# with
import pickle
with open("profile.pickle", "rb") as profile_file: # profile.pickel 파일을 profile_file 변수에 저장
    print(pickle.load(profile_file)) # close() 필요 없음

import pickle
with open("study.txt", "w", encoding="utf-8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요.")
with open("study.txt", "r", encoding="utf-8") as study_file:
    print(study_file.read())