## 기사 제목, 본문, 하이퍼링크를 txt 파일로 저장하기
## pandas 라이브러리를 활용하여 테이블 형식으로 데이터 확인

import os, re
import urllib.request as ur
from bs4 import BeautifulSoup as bs
import pandas as pd # pip install pandas
import numpy as np

title_list, url_list, content_list = [], [], []

newsUrl = 'https://news.daum.net/'
soup = bs(ur.urlopen(newsUrl).read(), 'html.parser')

## 파일 생성
f = open('article_total_2.txt', 'w', encoding='utf-8-sig')

for i in soup.find_all('div', {'class':'item_issue'}):
    # 제목 추출
    #f.write(i.text + '\n')
    title_list.append(i.text)

    # URL주소 추출
    #f.write(i.find_all('a')[0].get('href') + '\n')
    url_list.append(i.find_all('a')[0].get('href'))

    # 본문 추출을 위한 새로운 soup2 객체
    soup2 = bs(ur.urlopen(i.find_all('a')[0].get('href')).read(), 'html.parser')

    # 본문 추출
    tmp_content_list = []
    for j in soup2.find_all('div', {'class':'article_view'}):
        for k in j.find_all('p'):
            # f.write(k.text + '\n')
            content_list.append(k.text)
#f.close()

print(content_list)

## 불필요한 \n 없애기
title_list = [i.replace('\n', '') for i in title_list]

## title에서 기사 구분(section)만 따로 저장
section_list = [i[:2] for i in title_list]

## 양쪽끝 공백을 없애는 strip() 메서드를 활용하여 최종 title 저장
final_title_list = [i[2:].strip() for i in title_list]


# for i in range(len(section_list)):
#     f.write(section_list[i] + '\n')
#     f.write(final_title_list[i] + '\n')
#     f.write(content_list[i] + '\n')
# f.close()

## 참고 > https://dandyrilla.github.io/2017-08-12/pandas-10min/
## pandas 라이브러리를 통해 데이터 오브젝트 생성
## 자주 사용하는 데이터 오브젝트로는 Series와 DataFrame이 있다.
## 데이터를 담는 그릇의 '형태'에 따라 나뉘는데, Series는 1차원 배열(인덱스)로
## DataFrame은 2차원 배열(인덱스+컬럼)로 데이터를 담는다.

## .T 속성은 DataFrame에서 index와 column을 바꾼 형태의 DataFrame이다.
data = pd.DataFrame([section_list, final_title_list, url_list, content_list]).T

## DataFrame의 columns를 설정한다.
data.columns = ['section', 'title', 'url', 'content']

data.to_csv("title_source_01.csv", encoding='utf-8-sig', index=False)

## data.head() # DataFrame의 상위 5개 데이터를 보여준다.
## data.tail() # DataFrame의 하위 5개 데이터를 보여준다.
# print(data.head())