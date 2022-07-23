# Quiz7) 당신의 회사에서는 매주 1회 작성해야 하는 보고서가 있습니다.
# 보고서는 항상 아래와 같은 형태로 출력되어야 합니다.

# - X 주차 주간보고 -
# 부서 : 
# 이름 : 
# 업무 요약 : 

# 1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오.

# 조건 : 파일명은 '1주차.txt', '2주차.txt', ... 와 같이 만듭니다.

# 나는 1~3주차만 해봄 ㅋ
import pickle
for i in range(1, 4):
    with open(str(i) + "주차.txt", "w", encoding="utf-8") as week_report:
        week_report.write("- {0} 주차 주간보고 -".format(i))
        week_report.write("\n부서 : ")
        week_report.write("\n이름 : ")
        week_report.write("\n업무 요약 : ")

    with open(str(i) + "주차.txt", "r", encoding="utf-8") as week_report:
        print(week_report.read())
