from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
from datetime import date, timedelta, datetime

officeId = {
    "동아일보" : "020",
    "조선일보" : "023",
    "중앙일보" : "025",
    "한겨레" : "028",
    "경향일보" : "032",
}

today = datetime.today()
numdays = 7
date_list = [(today - timedelta(days=x)).strftime("%Y%m%d") for x in range(1, numdays)]

for day in date_list:
    url = f'https://news.naver.com/main/ranking/office.naver?officeId=020&date={day}'
    print(url)
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html, 'html.parser')

    rankingNews = soup.find('div', attrs={'class' : 'rankingnews_box_inner'})
    newsTitles = rankingNews.find_all('a', attrs={'class' : 'list_title nclicks(\'RBP.drnknws\')'})
    newsViews = rankingNews.find_all('span', attrs={'class' : 'list_view'})
    # for newsTitle in newsTitles:
    #     print(newsTitle.text)
    # for newsView in newsViews:
    #     print(newsView.text)