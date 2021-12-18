#!/usr/bin/env python
# coding: utf-8

# In[36]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#파일 불러오기
all_acc = pd.read_csv('C:/Users/PC/Desktop/주피터/데이터크롤링/교통사고 통계.csv',
                      sep=',',header = 0, engine = 'python',encoding = "cp949")

#x축 설정
colm = [2012,2013,2014,2015,2016,2017,2018,2019,2020]

#불러온 데이터에서 발생년도별로 갯수 추출해서 data 배열에 넣기
data = []
for i in range(2012, 2021):
    data.append(all_acc[all_acc.발생년도 == i].count()['발생년도'])
    
#그래프 그리기
plt.plot(colm,data,color = '#22AFC8')
plt.xlabel('년도')
plt.ylabel('사고 수')
plt.ylim(0,500)

plt.rcParams["font.family"] = 'NanumGothic'
plt.title('전체 사망교통사고')
plt.show()

