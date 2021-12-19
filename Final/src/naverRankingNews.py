from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
from datetime import date, timedelta, datetime

def getRankingNews(officeId, fromDays):
    result = []
    today = datetime.today()
    date_list = [(today - timedelta(days=x)) for x in range(1, fromDays)]
    for mediaName, mediaCode in officeId.items():
        for day in date_list:
            url = f'https://news.naver.com/main/ranking/office.naver?officeId={mediaCode}&date={day.strftime("%Y%m%d")}'
            print(url)
            html = urllib.request.urlopen(url)
            soup = BeautifulSoup(html, 'html.parser')

            rankingNews = soup.find('div', attrs={'class' : 'rankingnews_box_inner'})
            newsTitles = rankingNews.find_all('a', attrs={'class' : 'list_title nclicks(\'RBP.drnknws\')'})
            newsViews = rankingNews.find_all('span', attrs={'class' : 'list_view'})
            description = rankingNews.find_all('p', attrs={'class' : 'list_writing'})
            for newsTitle, newsView, description in zip(newsTitles, newsViews, description):
                result.append([mediaName, day.strftime('%Y-%m-%d'), newsTitle.text, newsView.text, description.text])
    return result

def exportResultToCsv(data):
    header = ['media', 'date', 'title', 'description', 'views']
    news_df = pd.DataFrame(data, columns=header)
    news_df.to_csv('./Final/output/rankingNewsDesc.csv', encoding='utf-8', mode='w', index=True)

def naverRankingNews():
    officeId = {
        "동아일보" : "020",
        "조선일보" : "023",
        "중앙일보" : "025",
        "한겨레" : "028",
        "경향일보" : "032",
    }
    days = 366
    
    print('Naver ranking news crawling START==========================================')
    result = getRankingNews(officeId, days)
    print('Naver ranking news crawling END  ==========================================')
    exportResultToCsv(result)
    
    del result[:]

if __name__ == '__main__':
    naverRankingNews()
