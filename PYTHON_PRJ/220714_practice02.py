## 포털 사이트에서 기사를 크롤링 한다.
## 활용 사이트는 https://news.daum.net/

## 웹 크롤링을 위한 기본 import
import os, re
import urllib.request as ur
from bs4 import BeautifulSoup as bs

newsUrl = 'https://news.daum.net/'
soup = bs(ur.urlopen(newsUrl).read(), 'html.parser')
# print("[print] >>> ", soup) # html 데이터 확인

## 첫번째 헤드라인만 추출해보기
# print("[print] >>>\n ", soup.find_all('div', {'class':'cont_thumb'})[0].text)

## 전체 목록의 헤드라인만 추출해보기
# for i in soup.find_all('div', {'class':'cont_thumb'}):
#     print(i.text)

## 하이퍼링크 주소를 추출할때는 <a> 태그의 href 속성값을 사용한다.
## find_all으로 지정한 태그 데이터를 가져와
## 그 안의 특정한 속성값을 찾아내기 위해 get메서드를 사용한다.
# print("get 제외 >> ", soup.find_all('a')[0])
# print("text 출력 >> ", soup.find_all('a')[0].text)
# print("get 활용 >> ", soup.find_all('a')[0].get('href'))

## get메서드를 활용해 URL 접속한 사이트의 <a>태그 > href 속성 데이터를 전체를 가져온다.
# for i in soup.find_all('a'):
#     print(i.get('href'))

## get메서드를 활용해 첫번째 기사 헤드라인의 <a>태그 > href 속성 데이터를 가져온다.
# print(soup.find_all('div', {'class':'item_issue'})[0].find_all('a')[0].get('href'))

## get메서드를 활용해 전체 기사 헤드라인의 <a>태그 > href 속성 데이터를 가져온다.
# for i in soup.find_all('div', {'class':'item_issue'}):
#     for j in i.find_all('a'):
#         print(j.get('href'))

## 기사 제목 추출하기
# print(soup.find_all('div', {'class':'cont_thumb'})[0].text.replace('\n', ''))
headline = soup.find_all('div', {'class':'item_issue'})
# for i in headline:
#     print(i.text.replace('\n', ''))


## 하나의 기사를 클릭하여 나오는 기사 내용 추출하기
articleUrl = 'https://v.daum.net/v/20220714134014647'
soup2 = bs(ur.urlopen(articleUrl).read(), 'html.parser')
# print(soup2)

## 기사 내용 추출하기
# for i in soup2.find_all('p'):
# for i in soup2.find_all('div', {'class':'article_view'}):
#     for j in i.find_all('p'):
#         print(j.text)


## 기사 제목과 기사 본문을 같이 추출하기(한건만)
# print(headline[0].text.replace('\n', ''))
# soup3 = bs(ur.urlopen(headline[0].find_all('a')[0].get('href')).read(), 'html.parser')
# articleDetails = soup3.find_all('div', {'class':'article_view'})
# for articleDetail in articleDetails:
#     for detail in articleDetail:
#         print(detail.text)
#     print('*'*100)

## 기사 제목과 기사 본문을 같이 추출하기(전체)
for i in headline:
    print(i.text.replace('\n', ''))
    soup3 = bs(ur.urlopen(i.find_all('a')[0].get('href')).read(), 'html.parser')
    articleDetails = soup3.find_all('div', {'class':'article_view'})
    for articleDetail in articleDetails:
        for detail in articleDetail.find_all('p'):
            print(detail.text)
        print('*'*100)