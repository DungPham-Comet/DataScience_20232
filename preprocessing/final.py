#!/usr/bin/env python
# coding: utf-8

# In[14]:


import pandas as pd


# In[15]:

def final():

    hacom = pd.read_csv('hacom.csv')


    # In[16]:


    hacom.head()


    # In[17]:


    ltw_vp = pd.read_csv('laptopworld_vp.csv')


    # In[18]:


    ltw_gm = pd.read_csv('laptopworld_gaming.csv')


    # In[19]:


    ltw = pd.concat([ltw_vp, ltw_gm], ignore_index=True)


    # In[20]:


    ltw.head()


    # In[21]:


    ltw.head()


    # In[22]:


    final = pd.concat([hacom, ltw], ignore_index=True)


    # In[23]:


    final.columns


    # In[24]:


    final.drop(columns=['screen_pixels','screen_full'], inplace=True)


    # In[25]:


    final.columns


    # In[26]:


    final.to_csv("final.csv", encoding="utf-8-sig")

