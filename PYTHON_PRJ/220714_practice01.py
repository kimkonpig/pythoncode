## 웹 HTML parsing을 통해 태그 접근하여 원하는 데이터를 가져온다.

## BeautifulSoup 설치 필요
## pip install beautifulsoup4

## urllib 라이브러리는 웹에서 얻은 데이터를 다루는 패키지이다.
## urllib 안에는 총 4개의 모듈이 있다.
## 그중 request 모듈을 사용해 웹문서를 열어 데이터를 읽어올 수 있다.
import urllib.request as ur
import os, re

## import 라이브러리 VS from 라이브러리 import 모듈
## import 라이브러리 : 라이브러리 전체를 가져온다.
## from 라이브러리 import 모듈 : 라이브러리 중에서 필요한 모듈만 가져온다.
from bs4 import BeautifulSoup as bs

## url이라는 객체에 URL주소 저장
url = 'https://quotes.toscrape.com/'

## requet모듈을 사용하여 URL주소에 해당하는 웹 사이트 불러오기
html = ur.urlopen(url)
# print("[print] html : ", html)

## read()를 활용하여 html에 있는 내용 확인(200자까지만)
# print("[print] html.read()[:200] : "html.read()[:200])

## beautifulsoup를 활용해 html 객체에 저장한 데이터의 정보를 쉽게 추출할 수 있는 형태
## 즉 parsing 하기 쉬운 형태로 변환한다. 결과는 Beautifulsoup 객체로 반환한다.
soup = bs(html, 'html.parser')
# print("[print] type(html) : ", type(html))
# print("[print] type(soup) : ", type(soup))

## beautifulsoup의 find_all 메서드로 원하는 태그만 추출할 수 있다.
## find_all 메서드는 '지정한' 태그로 둘러싸인 요소를 찾아 리스트 형태로 반환한다.
# print("[print] type(soup.find_all('span')) : ", type(soup.find_all('span')))
# print("[print] soup.find_all('span')[0] : ", soup.find_all('span')[0])

## find_all('').text 메서드를 통해 태그 안에 있는 text만 추출할 수 있다.
quote = soup.find_all('span')
# print("[print] quote[0] : ", quote[0])
# print("[print] quote[0].text : ", quote[0].text)

## for문을 통해 span > text 만 추출한다.
# for i in quote:
#    print(i.text)

## div 태그 안에 정의된 특정 클래스만 찾기
## class 속성이 quote인 <div> 태그에 들어있는 텍스트만 찾아 추출한다.
## \n과 같은 정규식 표현을 정제하여 보려면 print를 사용한다.
# print("[print] soup.find_all('div', {'class':'quote'})[0].text : ", soup.find_all('div', {'class':'quote'})[0].text)

## for문을 통해 <div>태그 > class=quote인 엘리먼트의 텍스트만 추출한다.
# for i in soup.find_all('div', {'class':'quote'}):
# print("[print] text : ", i.text)
# print('*' * 100)