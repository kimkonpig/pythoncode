## 추출한 데이터를 텍스트 파일로 저장하기
## 220714_practice02.py 코드 활용

import os, re
import urllib.request as ur
from bs4 import BeautifulSoup as bs

newsUrl = 'https://news.daum.net/'
soup = bs(ur.urlopen(newsUrl).read(), 'html.parser')

## URL 주소를 txt 파일로 저장하기
href_list = []
for i in soup.find_all('div', {'class':'item_issue'}):
    for j in i.find_all('a'):
        href_list.append(j.get('href'))

## 파일 생성
# f = open("links.txt", "w")

## 파일 쓰기
## for i in href_list: # 처음부터 끝까지
## href_list 배열의 처음부터 끝까지 2간격으로
# for i in href_list[::2]:
#     f.write(i+'\n')

## 파일 닫기
## 꼭 닫아주어야 한다. 닫지 않으면 저장이 안될수도 있음
# f.close()


## 기사 본문을 txt 파일로 저장하기
## 일단 기사 하나로 테스트
articleUrl = 'https://v.daum.net/v/20220714134014647'
soup2 = bs(ur.urlopen(articleUrl).read(), 'html.parser')

## 파일 생성
# f = open('article_1.txt', 'w', encoding='utf-8-sig')

# for i in soup2.find_all('div', {'class':'article_view'}):
#     for j in i.find_all('p'):
#         f.write(j.text + '\n')

# f.close()