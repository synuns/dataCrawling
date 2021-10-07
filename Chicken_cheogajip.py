import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
import datetime
from itertools import count
import xml.etree.ElementTree as ET
import ssl

def get_request_url(url, enc='utf-8'):
    
    req = urllib.request.Request(url)

    try:
        ssl._create_default_https_context = ssl._create_unverified_context

        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            try:
                rcv = response.read()
                ret = rcv.decode(enc)
            except UnicodeDecodeError:
                ret = rcv.decode(enc, 'replace')    
            
            return ret
            
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None



def CheogajipAddress(result):
    for page_idx in range(0,101):
        Cheogajip_URL = 'http://www.cheogajip.co.kr/bbs/board.php?bo_table=store&page=%s'  % str(page_idx+1)   
        print (Cheogajip_URL)
        response = urllib.request.urlopen(Cheogajip_URL)
        soupData = BeautifulSoup(response, 'html.parser')
        tbody_tag = soupData.find('tbody')

        for store_tr in tbody_tag.findAll('tr'):
            tr_tag = list(store_tr.strings)
            store_name = tr_tag[3]
            store_address = tr_tag[5]
            store_sido_gu = store_address.split()[:2]
            result.append([store_name] + store_sido_gu + [store_address])
           

     #return
    
   



def cswin_Cheogajip():

    result = []

    print('CHEOGAJIP ADDRESS CRAWLING START')
    CheogajipAddress(result)
    cheogajip_table = pd.DataFrame(result, columns=('store', 'sido', 'gungu', 'store_address'))
    cheogajip_table.to_csv("./cheogajip.csv", encoding="cp949", mode='w', index=True)
    del result[:]


    print('FINISHED')
    
if __name__ == '__main__':
     cswin_Cheogajip()


