#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import seaborn as sns
import statsmodels.api as sm


# In[2]:


bedal_df = pd.read_csv('./배달앱_및_배달대행_이용현황_20211021201746.csv', sep=',', header=None, engine='python', encoding='utf-8')
bedal_df = bedal_df.transpose()
bedal_df = bedal_df.drop(index=0, axis=0)
bedal_df.columns = ['year', 'using', 'whether_or_not', 'percentage']
bedal_df['whether_or_not']=bedal_df['whether_or_not'].apply(lambda x:x.replace("예","Yes"))
bedal_df['whether_or_not']=bedal_df['whether_or_not'].apply(lambda x:x.replace("아니오","No"))
bedal_df.to_csv('./output/bedal_use.csv')


# In[3]:


app_bedal_df = bedal_df[bedal_df['using']=='배달앱']
proxy_bedal_df = bedal_df[bedal_df['using']=='배달대행']
print(app_bedal_df)
print(proxy_bedal_df)


# In[174]:


plt.figure(figsize=(8,6))
sns.set_style('whitegrid')
ax1 = plt.plot()
ax1 = sns.barplot(data=app_bedal_df, x='year',y='percentage', hue='whether_or_not')
plt.title('delivery app')
plt.legend(loc='upper right')
plt.savefig('delivery_app.png')


# In[175]:


plt.figure(figsize=(8,6))
ax2 = plt.plot()
ax2 = sns.barplot(data=proxy_bedal_df, x='year',y='percentage', hue='whether_or_not')
plt.title('delivery proxy')
plt.legend(loc='upper right')
plt.show()
plt.savefig('delivery_proxy.png')


# In[7]:


sns.FacetGrid(bedal_df, col = 'using', row = 'year').map(sns.barplot, 'percentage')


# In[ ]:




