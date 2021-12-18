from bs4 import BeautifulSoup
import urllib.request
import pandas as pd

url = "https://news.naver.com/main/ranking/office.naver?officeId=020&date=20211217"

html = urllib.request.urlopen(url)
soup = BeautifulSoup(html, 'html.parser')

rankingNews = soup.find('div', attrs={'class' : 'rankingnews_box_inner'})
newsTitles = rankingNews.find_all('a', attrs={'class' : 'list_title nclicks(\'RBP.drnknws\')'})
newsViews = rankingNews.find_all('span', attrs={'class' : 'list_view'})

for newsTitle in newsTitles:
    print(newsTitle.text)

for newsView in newsViews:
    print(newsView.text)