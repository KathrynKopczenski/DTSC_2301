#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import pandas as pd
from bs4 import BeautifulSoup


# In[7]:


url = "https://webpages.charlotte.edu/mscipion/"

r= requests.get(url)
print(r)


# In[11]:


soup = BeautifulSoup(r.text, "lxml")
soup


# In[12]:


table = soup.find("table")
print(table)


# In[13]:


headers = table.find_all("th")
print(headers)


# In[14]:


titles = []

for i in headers:
    title = i.text
    titles.append(title)
    
print(titles)


# In[15]:


df= pd.DataFrame(columns=titles)
print(df)


# In[16]:


rows = table.find_all("tr")
print(rows)


# In[17]:


for i in rows[1:]:
    print(i) 


# In[18]:


for i in rows[1:]:
    data = table.find_all("td")
    print(data)


# In[19]:


for i in rows[1:]:
    data = table.find_all("td")
    print(data)
    row = [tr.text for tr in data]
    print(row)


# In[20]:


for i in rows[1:]:
    data = i.find_all("td")            
    row = [tr.text for tr in data]     
    l =len(df)                         
    df.loc[l]= row                     

df.head(10) 

