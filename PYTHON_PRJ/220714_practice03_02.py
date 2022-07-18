## 기사 제목, 본문, 하이퍼링크를 txt 파일로 저장하기
## 파일 생성하여 바로 write (article_total.txt)

import os, re
import urllib.request as ur
from bs4 import BeautifulSoup as bs

newsUrl = 'https://news.daum.net/'
soup = bs(ur.urlopen(newsUrl).read(), 'html.parser')

## 파일 생성
f = open('article_total.txt', 'w', encoding='utf-8-sig')

for i in soup.find_all('div', {'class':'item_issue'}):
    try:
        # 제목 추출
        f.write(i.text + '\n')

        # URL주소 추출
        f.write(i.find_all('a')[0].get('href') + '\n')

        # 본문 추출을 위한 새로운 soup2 객체
        soup2 = bs(ur.urlopen(i.find_all('a')[0].get('href')).read(), 'html.parser')

        # 본문 추출
        for j in soup2.find_all('div', {'class':'article_view'}):
            for k in j.find_all('p'):
                f.write(k.text + '\n')
    
    except:
        pass

f.close()  
