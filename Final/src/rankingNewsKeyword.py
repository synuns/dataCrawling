#!/usr/bin/env python
# coding: utf-8

# In[9]:


import re
import pandas as pd
from konlpy.tag import Okt

nlp = Okt()

file = 'rankingNewsDesc.csv'
data_frame = pd.read_csv(file, sep=',',header = 0, engine = 'python',encoding = "utf-8")


# In[10]:


data_frame


# In[51]:


data_frame['title'] = data_frame['title'].apply(lambda x : re.sub(r'[^ ㄱ-ㅣ가-힣]+', " ", str(x)))
data_frame['description'] = data_frame['description'].apply(lambda x : re.sub(r'[^ ㄱ-ㅣ가-힣]+', " ", str(x)))

data_frame.head()


# In[52]:


title_keyword = []
desc_keyword = []

for item in data_frame['title']:
    title_keyword.append(nlp.nouns(item))

for item in data_frame['description']:
    desc_keyword.append(nlp.nouns(item))


# In[56]:


data_frame['title'] = title_keyword
data_frame['description'] = desc_keyword


# In[57]:


data_frame


# In[58]:


data_frame.to_csv('./rankingNewsKeyword.csv', sep=',')


# In[ ]:




