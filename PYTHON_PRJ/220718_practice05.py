## 네이버 크롤링 실습
## 네이버 금융페이지에서 코스피 200 종목 찾기
## 각 종목의 링크에서 시가 총액, 현재 주가, 전일 주가 추출
## 전일대비 가격 계산하기
## 활용링크 : https://finance.naver.com/sise/entryJongmok.nhn?&page=
## page 파라미터로 1~20까지 입력하면 200개의 종목 확인 가능

## 코스피 200 종목에서 종목코드, 이름, 링크 저장

from os import link
import requests
import re
import pandas as pd
from bs4 import BeautifulSoup

## 활용URL
baseUrl = 'https://finance.naver.com/sise/entryJongmok.nhn?&page='

## 추출데이터 리스트
code_list, name_list, link_list = [], [], []

for i in range(1, 21): # 1부터 20까지 반복
    url = baseUrl + str(i)
    r1 = requests.get(url)
    soup1 = BeautifulSoup(r1.text, 'lxml')
    # Couldn't find a tree builder with the features you requested: lxml. Do you need to install a parser library?
    # pip install lxml

    items = soup1.find_all('td', {'class':'ctg'})
    for item in items:
        txt = item.a.get('href') # /item/main.naver?code=005930
        k = re.search('[\d]+', txt) # 정규표현식을 통해 문자열에서 정수만 추출

        if k:
            code = k.group()
            code_list.append(code)

            name = item.text
            name_list.append(name)

            url = "https://finance.naver.com" + txt
            link_list.append(url)

data = pd.DataFrame([code_list, name_list, link_list], index=['code', 'name', 'link']).T
# print(data.head())


## 각 종목의 링크에서 시가 총액, 현재 주가, 전일 주가 추출

##일단 첫번째 종목으로 해보기
# r2 = requests.get(link_list[0])
# soup2 = BeautifulSoup(r2.text, 'lxml')

# market_cap = soup2.find_all('tr', {'class':'strong'})[0].text.replace('\n', '').replace('\t', '')


# # 뒤에 span blind가 뭔지 모르겠다 ㅠㅠ
# today_price = soup2.find_all('div', {'class':'today'})[0].find('span', {'class':'blind'}).text

# previos_price = soup2.find_all('td', {'class':'first'})[0].find('span', {'class':'blind'}).text

# print("market_cap : ", market_cap)
# print("today_price : ", today_price)
# print("previos_price : ", previos_price)

market_cap_list, today_price_list, previous_price_list, rate_list = [], [], [], []
for url in link_list:
    r2 = requests.get(url)
    soup2 = BeautifulSoup(r2.text, 'lxml')

    market_cap = soup2.find_all('tr', {'class':'strong'})[0].text.replace('\n', '').replace('\t', '')
    market_cap_list.append(market_cap)

    today_price = soup2.find_all('div', {'class':'today'})[0].find('span', {'class':'blind'}).text
    today_price_list.append(today_price)

    previous_price = soup2.find_all('td', {'class':'first'})[0].find('span', {'class':'blind'}).text
    previous_price_list.append(previous_price)

data = pd.DataFrame([code_list, name_list, link_list, market_cap_list, today_price_list, previous_price_list, rate_list]).T
data.columns = ['code', 'name', 'link', 'market_cap', 'today_price', 'previous_price', 'rate']

# 189번째까지는 원래 데이터, 이후 11개는 데이터가 0으로 들어감
# test_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,6,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34]
# print(test_list[:10] + [0 for i in range(11)])

data['market_cap'] = market_cap_list[:189] + [0 for i in range(11)]
data['today_price'] = today_price_list[:189] + [0 for i in range(11)]
data['previous_price'] = previous_price_list[:189] + [0 for i in range(11)]

# print(data.head())

new_market_cap, new_today_list, new_previous_list = [], [], []
for i in data['market_cap']:
    try:
        new_market_cap.append(i.replace('시가총액', ''))
    except:
        new_market_cap.append(i)

for i in data['today_price']:
    try:
        new_today_list.append(int(i.replace(',', '')))
    except:
        new_today_list.append(i)

for i in data['previous_price']:
    try:
        new_previous_list.append(int(i.replace(',', '')))
    except:
        new_previous_list.append(i)

data['market_cap'] = new_market_cap
data['today_price'] = new_today_list
data['previous_price'] = new_previous_list
data['rate'] = [round(i*100, 2) for i in 1 - (data['previous_price'] / data['today_price'])]

address = 'C:\\pythoncode\\PYTHON_PRJ\\'
data.to_csv(address + "title_source_03.csv", encoding='utf-8-sig', index=False)

