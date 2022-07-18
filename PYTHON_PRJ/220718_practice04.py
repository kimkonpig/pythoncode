## 네이버 뉴스기사 수집하기

import requests
import urllib.request as ur
from bs4 import BeautifulSoup as bs
import pandas as pd

search_word = "데이터"
raw = requests.get("https://search.naver.com/search.naver?where=news&query=" + search_word,
                    headers={'User-Agent':'Mozilla/5.0'});
html = bs(raw.text, "html.parser")

articles = html.select("ul.list_news > li")
# print(articles[0])

## 첫번째 기사에 대한 제목과 언론사 추출
title = articles[0].find('a', {'class':'news_tit'}).text
source = articles[0].find('a', {'class':'info press'}).text
# print(title)
# print(source)

## 반복하여 전체 기사의 제목과 언론사 추출
title_list = []
source_list = []
url_list = []
content_list = []

for i in range(len(articles)):
    title_list.append(articles[i].find('a', {'class':'news_tit'}).text)
    source_list.append(articles[i].find('a', {'class':'info press'}).text)
    url_list.append(articles[i].find('a', {'class':'news_tit'}).get('href'))

    print(url_list[i])

    raw_content = requests.get(url_list[i], headers={'User-Agent':'Mozilla/5.0'})
    html_content = bs(raw_content.text, "html.parser")

    # 각 뉴스 본문마다 태그가 다르게 되어있어서 동일한 태그로는 추출할 수 없음
    for j in html_content.find_all('article', {'class':'story-news'}):
        total_content = ''
        for k in j.find_all('p'):
            total_content += k.text
        content_list.append(total_content)

data = pd.DataFrame([source_list, title_list, url_list, content_list]).T
data.columns = ['source', 'title', 'url', 'content']

data.to_csv("title_source_02.csv", encoding='utf-8-sig', index=False)
# print(data.head())
