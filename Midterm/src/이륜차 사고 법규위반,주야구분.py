#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import seaborn as sns
import statsmodels.api as sm
import json


# In[2]:


df = pd.read_csv('./output/traffic_accident.csv', sep = ',', header = 0, engine = 'python')


# In[3]:


# font_list = [font.name for font in fm.fontManager.ttflist]
# print(font_list)
# print(mpl.matplotlib_fname())
plt.rc("font", family="NanumGothic")
sns.set(font="NanumGothic", 
        rc={"axes.unicode_minus":False},
        style='darkgrid')
fm._rebuild()


# In[4]:


# 사고유형 구분
acc_ty_df = df[['acc_year', 'wrngdo_isrty_vhcty_lclas_cd', 'dmge_isrty_vhcty_lclas_cd', 'aslt_vtr_cd']]
acc_ty_df = acc_ty_df.astype({'acc_year': 'str', 'wrngdo_isrty_vhcty_lclas_cd': 'str', 'dmge_isrty_vhcty_lclas_cd': 'str', 'aslt_vtr_cd': 'str'})
# 주야 사고 구분
dfht_ty_df = df[['acc_year', 'wrngdo_isrty_vhcty_lclas_cd', 'dmge_isrty_vhcty_lclas_cd', 'dght_cd']]
dfht_ty_df = dfht_ty_df.astype({'acc_year': 'str', 'wrngdo_isrty_vhcty_lclas_cd': 'str', 'dmge_isrty_vhcty_lclas_cd': 'str', 'dght_cd': 'str'})


# In[5]:


acc_ty_df.columns = ['발생년도', '가해자', '피해자', '법규위반']
vehicleTypeCode = {'1':'승용차', '2':'승합차', '3':'화물차', '4':'특수차', '5':'이륜차','6':'사륜오토바이','7':'원동기장치자전거','8':'자전거','9':'개인형이동수단','10':'건설기계','11':'농기계','12':'보행자','98':'기타','99':'불명','Z1':'열차','ZL':'기타','##':'없음'}
victim_vehicleTypeCode = {'01':'승용차', '02':'승합차', '03':'화물차', '04':'특수차', '05':'이륜차','06':'사륜오토바이','07':'원동기장치자전거','08':'자전거','09':'개인형이동수단','10':'건설기계','11':'농기계','12':'보행자','98':'기타','99':'불명','Z1':'열차','ZL':'기타','##':'없음'}
violationTypeCode = {'1':'과속', '2':'중앙선침범', '3':'신호위반', '4':'안전거리미확보','5':'안전운전 의무 불이행','6':'교차로 통행방법 위반','7':'보행자 보호의무 위반','99':'기타'}
acc_ty_df = acc_ty_df.replace({'가해자' : vehicleTypeCode})
acc_ty_df = acc_ty_df.replace({'피해자' : victim_vehicleTypeCode})
acc_ty_df = acc_ty_df.replace({'법규위반' : violationTypeCode})
acc_ty_df.to_csv('./output/사고유형구분.csv', index=False)


# In[6]:


acc_ty_df


# In[12]:


plt.figure(figsize = (15,8))
motorcycle_acc_ty_df = acc_ty_df.loc[acc_ty_df['가해자'] == '이륜차']
sns.countplot(data=motorcycle_acc_ty_df, x='발생년도', hue='법규위반', dodge=False)
plt.savefig('./output/violence_overlap.png')


# In[14]:


plt.figure(figsize = (15,8))
sns.countplot(data=motorcycle_acc_ty_df, x='발생년도', hue='법규위반')
plt.savefig('./output/violence.png')


# In[15]:


dfht_ty_df.columns = ['발생년도', '가해자', '피해자', '주야']
dayNightCode = {'1':'주', '2':'야'}
dfht_ty_df = dfht_ty_df.replace({'주야' : dayNightCode})
dfht_ty_df = dfht_ty_df.replace({'가해자' : vehicleTypeCode})
dfht_ty_df = dfht_ty_df.replace({'피해자' : vehicleTypeCode})
dfht_ty_df.to_csv('./output/주야구분.csv', index=False)


# In[16]:


dfht_ty_df


# In[17]:


plt.figure(figsize = (15,8))
motorcycle_dfht_ty_df = dfht_ty_df.loc[dfht_ty_df['가해자'] == '이륜차']
sns.countplot(data=motorcycle_dfht_ty_df, x='발생년도', hue='주야')
plt.savefig('./output/daynight.png')


# In[ ]:





# In[ ]:




