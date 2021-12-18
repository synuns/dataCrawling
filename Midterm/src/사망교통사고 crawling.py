#!/usr/bin/env python
# coding: utf-8

# In[26]:


## import os
import sys
import urllib.request
import datetime
import time
import json
import pandas as pd

#개인 서비스키 사용!
ServiceKey="th4V9rxccPnhCi8wtKy6tvs2C0HWCyjpHlDxDFoVpBKqkFXvT5u2%2BhO9jdokE7gcPEGdjrWxI2r%2BCtOWdsEnWA%3D%3D"

#[CODE 1]
def getRequestUrl(url):    
    req = urllib.request.Request(url)    
    try: 
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print ("[%s] Url Request Success" % datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None


#[CODE 2]
def getAccidentItem(year, sido_code, gugun_code,pageNo):    
    service_url = "http://apis.data.go.kr/B552061/AccidentDeath/getRestTrafficAccidentDeath"
    parameters = "?ServiceKey=" + ServiceKey        #인증키
    parameters += "&searchYear=" + str(year)        #년도
    parameters += "&siDo=" + str(sido_code)         #시도 코드
    parameters += "&guGun=" + str(gugun_code)       #군구 코드
    parameters += "&type=json"                      #datatype = json
    parameters += "&numOfRows=1"                    #항목 수
    parameters += "&pageNo=" + str(pageNo)          #페이지 번호
        
    url = service_url + parameters
    
    retData = getRequestUrl(url)   #[CODE 1]
    
    if (retData == None):
        return None
    else:
         return json.loads(retData)

#[CODE 3]
def getAccidentService(nStartYear, nEndYear):
    jsonResult = []
    result = []   
    pageNo = 1
    
    for year in range(nStartYear, nEndYear+1):
        for gugun in range(1101, 1126):
            while 1 :
                jsonData = getAccidentItem(year, 1100, gugun,pageNo) #[CODE 2]
                pageNo += 1
                if(jsonData==None):
                    pageNo = 0
                    break
                if (jsonData['resultMsg'] == 'NORMAL_CODE'):                
                    # 더이상 제공되는 데이터가 없는 마지막 항목인 경우 -----------------------------------
                    if jsonData['numOfRows'] == 0:
                        pageNo = 0
                        break                
                    
                    #jsonData를 출력하여 확인......................................................
                    print (json.dumps(jsonData, indent=4,sort_keys=True, ensure_ascii=False))
                    
                    #저장할 내용(코드)들
                    acc_typ = jsonData['items']['item'][0]['acc_ty_lclas_cd']             #사고유형대분류
                    dght_cd = jsonData['items']['item'][0]['dght_cd']                     #주야구분코드
                    aslt_vtr_cd = jsonData['items']['item'][0]['aslt_vtr_cd']             #가해자법규위반코드
                    wrn_cd = jsonData['items']['item'][0]['wrngdo_isrty_vhcty_lclas_cd']  #가해당사자종별
                    dmg_cd = jsonData['items']['item'][0]['dmge_isrty_vhcty_lclas_cd']    #피해당사자종별
                    
                    print('----------------------------------------------------------------------')                
                    jsonResult.append({'year': year, 'acc_typ': acc_typ,'wrn_cd': wrn_cd, 
                                       'dmg_cd': dmg_cd, 'dght': dght_cd, 'aslt_cd':aslt_vtr_cd})
                    result.append([year, acc_typ, wrn_cd, dmg_cd,dght_cd,aslt_vtr_cd])
    return (jsonResult, result)

#[CODE 0]
def main():
    jsonResult = []
    result = []
    
    print("<< 서울 시내의 2012~2020년 사망교통사고 정보를 수집합니다. >>")    
    nStartYear = 2012
    nEndYear = 2020
    
    jsonResult, result = getAccidentService(nStartYear, nEndYear) #[CODE 3]

    if (jsonResult=='') : #URL 요청은 성공하였지만, 데이터 제공이 안된 경우
        print('데이터가 전달되지 않았습니다. 공공데이터포털의 서비스 상태를 확인하기 바랍니다.')
    else:
        #파일저장 1 : json 파일       
        with open('./교통사고 통계.json', 'w', encoding='utf8') as outfile:
            jsonFile  = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
            outfile.write(jsonFile)
        #파일저장 2 : csv 파일   
        columns = ["발생년도", "사고타입", "가해측", "피해측","주야코드","가해법규위반"]
        result_df = pd.DataFrame(result, columns = columns)
        result_df.to_csv('./교통사고 통계.csv',index=False, encoding='cp949')
    
if __name__ == '__main__':
    main()
