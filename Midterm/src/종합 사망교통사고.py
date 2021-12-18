#!/usr/bin/env python
# coding: utf-8

# In[51]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#파일 불러오기
all_acc = pd.read_csv('./교통사고 통계.csv',
                      sep=',',header = 0, engine = 'python',encoding = "cp949")

#x축
colm = [2012,2013,2014,2015,2016,2017,2018,2019,2020]

#이륜차 조건(코드 == 05)
condition = ((all_acc['가해측'] == '05') | (all_acc['피해측'] == '05'))
mot_acc = all_acc[condition]

#불러온 데이터에서 발생년도별로 갯수 추출해서 data 배열에 넣기
data1 = []
data2 = []
for i in range(2012, 2021):
    data1.append(all_acc[all_acc.발생년도 == i].count()['발생년도'])
    data2.append(mot_acc[mot_acc.발생년도 == i].count()['발생년도'])
    
#그래프 그리기
plt.plot(colm,data1,color = '#22AFC8',label = '전체')
plt.plot(colm,data2,color = '#AF22C8',label = '이륜차')
plt.legend(loc=1)
plt.xlabel('년도')
plt.ylabel('사고 수')
plt.ylim(0,450)

plt.rcParams["font.family"] = 'NanumGothic'
plt.title('사망교통사고')
plt.show()

