## 모듈
# # 방법1
# import practice_nado_08_theater as mv
# mv.price(3) # 3명이서 영화 보러 갔을 때 가격
# mv.price_morning(4) # 4명이서 조조할인영화 보러 갔을 때
# mv.price_soldier(5) # 5명이서 군인할인영화 보러 갔을 때

# # 방법 2
# from practice_nado_08_theater import *
# # from random import *
# price(3)
# price_morning(4)
# price_soldier(5)

# # 방법 3
# from practice_nado_08_theater import price, price_morning
# price(5)
# price_morning(6)
# price_soldier(7) # error

# # 방법 4
# from practice_nado_08_theater import price_soldier as ps
# ps(4)

##########################################################
## 패키지 : 모듈의 집합

# import travel.thailand # 클래스 이름은 작성X
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel.thailand import ThailandPackage # 클래스 이름까지 작성 가능
# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()


##########################################################
## __all__

# from travel import *
# trip_to = vietnam.VietnamPackage() # __init__ 파일에서 __all__ 지정을 해주어야함
# trip_to.detail()

# trip_to = thailand.ThailandPackage()
# trip_to.detail() # 얘는 에러남


##########################################################
## 모듈 직접 실행

# from travel import thailand
# trip_to = thailand.ThailandPackage()
# trip_to.detail()


##########################################################
## 패키지, 모듈 위치
# import inspect
# import random
# print(inspect.getfile(random))

# from travel import thailand
# print(inspect.getfile(thailand)) # c:\pythoncode\nadocoding_python\travel\thailand.py


##########################################################
## pip install
# # google에 pypi 검색
# # beautifulsoup4 설치
# # 터미널에 pip install beautifulsoup4 입력
# from bs4 import BeautifulSoup
# soup = BeautifulSoup("<p>Som<b>bad<i>HTML")
# print(soup.prettify())

# pip list 입력 시 설치되어있는 패키지 확인 가능
# pip show beautifulsoup4  패키지에 대한 정보
# pip install --upgrade beautifulsoup4 패키지 업그레이드
# pip uninstall beautifulsoup4 패키지 삭제


##########################################################
## 내장함수
# # input : 사용자 입력을 받는 함수
# language = input("무슨 언어를 좋아하세요?")
# print("{0}은 아주 좋은 언어입니다!".format(language))

# # dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
# print(dir())
# import random # 외장함수
# print(dir())
# import pickle
# print(dir())

# from random import random
# print(dir(random))

# lst = [1,2,3]
# print(dir(lst))

# name = 'jim'
# print(dir(name))

# list of python built in -> google 검색

## 외장함수
# # list of python modules -> google 검색
# # glob : 경로 내의 폴더 / 파일 목록 조회 (윈도우 dir 명령어)
# import glob
# print(glob.glob("nadocoding_python/*.py")) # 확장자가 py 인 모든 파일

# # os : 운영체제에서 제공하는 기본 기능
# import os
# print(os.getcwd()) # 현재 디렉토리

# folder = "sample_dir"

# if os.path.exists(folder):
#     print("이미 존재하는 폴더입니다.")
#     os.rmdir(folder)
#     print(folder, "폴더를 삭제하였습니다.")
# else:
#     os.makedirs(folder) # 폴더 생성
#     print(folder, "폴더를 생성하였습니다.")
# print(os.listdir())

# # time : 시간 관련 함수
# import time
# print(time.localtime())
# print(time.strftime("%Y-%m-%d %H:%M:%S"))

import datetime
# print("오늘 날짜는", datetime.date.today())

# timedelta : 두 날짜 사이의 간격
today = datetime.date.today() # 오늘날짜
td = datetime.timedelta(days=100) # 100일
print("우리가 만난지 100일은", today + td)