#!/usr/bin/env python
# coding: utf-8

# In[19]:


import re
import pandas as pd
from konlpy.tag import Okt

nlp = Okt()

file = 'rankingNewsDesc.csv'
data_frame = pd.read_csv(file, sep=',',header = 0, engine = 'python',encoding = "utf-8")


# In[20]:


data_frame


# In[21]:


data_frame['title'] = data_frame['title'].apply(lambda x : re.sub(r'[^ ㄱ-ㅣ가-힣]+', " ", str(x)))
data_frame['description'] = data_frame['description'].apply(lambda x : re.sub(r'[^ ㄱ-ㅣ가-힣]+', " ", str(x)))

data_frame.head()


# In[22]:


title_keyword = []
desc_keyword = []

for item in data_frame['title']:
    title_keyword.append(nlp.nouns(item))

for item in data_frame['description']:
    desc_keyword.append(nlp.nouns(item))


# In[23]:


title_keyword_except_one = []
desc_keyword_except_one = []

for keywords in title_keyword:
    _keyword = [keyword for keyword in keywords if len(keyword) > 1]
    title_keyword_except_one.append(_keyword)

for keywords in desc_keyword:
    _keyword = [keyword for keyword in keywords if len(keyword) > 1]
    desc_keyword_except_one.append(_keyword)


# In[26]:


data_frame['title'] = title_keyword_except_one
data_frame['description'] = desc_keyword_except_one


# In[27]:


data_frame


# In[28]:


data_frame.to_csv('./rankingNewsKeyword.csv', sep=',')


# In[ ]:




