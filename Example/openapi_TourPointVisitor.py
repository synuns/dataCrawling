import os
import sys
import urllib.request
from datetime import datetime
import time
import json
import math
import config

#[CODE 1]
def getRequestUrl(url):
    
    req = urllib.request.Request(url)
    
    try: 
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print ("[%s] Url Request Success" % datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" % (datetime.now(), url))
        return None

#[CODE 2]
def getTourPointVisitor(yyyymm, sido, gungu, nPagenum, nItems):

    end_point = "http://openapi.tour.go.kr/openapi/service/TourismResourceStatsService/getPchrgTrrsrtVisitorList"                
    ServiceKey = config.Service_Example_Key
    parameters = "?_type=json&serviceKey=" + ServiceKey
    parameters += "&YM=" + yyyymm
    parameters += "&SIDO=" + urllib.parse.quote(sido)
    parameters += "&GUNGU=" + urllib.parse.quote(gungu)
    parameters += "&RES_NM=&pageNo=" + str(nPagenum)
    parameters += "&numOfRows=" + str(nItems)

    url = end_point + parameters
    
    retData = getRequestUrl(url) #[CODE 1] 호출 
    
    if (retData == None):
        return None
    else:
        return json.loads(retData)

#[CODE 3]
def getTourPointData(item, yyyymm, jsonResult):
    
    addrCd = 0 if 'addrCd' not in item.keys() else item['addrCd']
    gungu = '' if 'gungu' not in item.keys() else item['gungu']
    sido = '' if 'sido' not in item.keys() else item['sido']
    resNm = '' if 'resNm' not in item.keys() else item['resNm']
    rnum = 0 if 'rnum' not in item.keys() else item['rnum']
    ForNum = 0 if 'csForCnt' not in item.keys() else item['csForCnt']
    NatNum = 0 if 'csNatCnt' not in item.keys() else item['csNatCnt']
    
    jsonResult.append({'yyyymm': yyyymm, 'addrCd': addrCd,
                    'gungu': gungu, 'sido': sido, 'resNm': resNm, 
                    'rnum': rnum, 'ForNum': ForNum, 'NatNum': NatNum})
    return    

#[CODE 0]
def csWin_TourPoint():

    jsonResult = []

    sido = '서울특별시'
    gungu = ''
    nPagenum = 1
    nTotal = 0
    nItems = 100
    
    nStartYear = 2011
    nEndYear = datetime.today().year 

    for year in range(nStartYear, nEndYear+1):
        for month in range(1, 13):

            yyyymm = "{0}{1:0>2}".format(str(year), str(month))

            nPagenum = 1

            # 데이터 요청 및 항목 추출 작업 반복            
            while True:
                #[CODE 2] 호출 
                jsonData = getTourPointVisitor(yyyymm, sido, gungu, nPagenum, nItems)
    
                if (jsonData['response']['header']['resultMsg'] == 'OK'):
                    nTotal = jsonData['response']['body']['totalCount']
            
                    if nTotal == 0:
                        break

                    for item in jsonData['response']['body']['items']['item']:
                        getTourPointData(item, yyyymm, jsonResult)  #[CODE 3] 호출
                        
                    nPage = math.ceil(nTotal / 100)            
                    
                    if (nPagenum == nPage):
                        break

                    nPagenum += 1
                
                else:
                    break
    
    with open('./data/%s_관광지입장정보_%d_%d.json' % (sido, nStartYear, nEndYear), 'w', encoding='utf8') as outfile:
        retJson = json.dumps(jsonResult,
                        indent=4, sort_keys=True,
                        ensure_ascii=False)
        outfile.write(retJson)
        
    print ('%s_관광지입장정보_%d_%d.json SAVED' % (sido, nStartYear, nEndYear))            

    
if __name__ == '__main__':
    csWin_TourPoint()
