#!/usr/bin/env python
# coding: utf-8

# In[205]:


import pandas as pd


# In[206]:

def final():

    hacom = pd.read_csv('../database/preprocessing/hacom.csv')


    # In[207]:


    hacom.head()


    # In[208]:


    ltw_vp = pd.read_csv('../database/preprocessing/laptopworld_vp.csv')


    # In[209]:


    ltw_gm = pd.read_csv('../database/preprocessing/laptopworld_gaming.csv')


    # In[210]:


    ltw = pd.concat([ltw_vp, ltw_gm], ignore_index=True)


    # In[211]:


    ltw.head()


    # In[212]:


    ltw.head()


    # In[213]:


    final = pd.concat([hacom, ltw], ignore_index=True)


    # In[214]:


    final.columns


    # In[215]:


    final.drop(columns=['screen_pixels','screen_full'], inplace=True)


    # In[216]:


    final.columns


    # In[217]:


    final['name'].value_counts()


    # In[218]:


    subset_columns = [col for col in final.columns if col not in ['name', 'price']]


    # In[219]:


    final.drop_duplicates(subset=subset_columns)


    # In[220]:


    final['os'].value_counts()


    # In[221]:


    final.loc[final['os'].isin(['Windows 11', 'Windows 11', 'Windows® 11']), 'os'] = 'Windows 11'
    final.loc[final['os'].isin(['NoOS', 'No OS']), 'os'] = 'NoOS'


    # In[222]:


    final['os'].value_counts()


    # In[223]:


    final['brand'].value_counts()


    # In[224]:


    final.loc[final['brand'].isin(['Acer', 'Acer ']), 'brand'] = 'Acer'
    final.loc[final['brand'].isin(['Lenovo', 'Lenovo ']), 'brand'] = 'Lenovo'


    # In[225]:


    final['brand'].value_counts()


    # In[226]:


    counts = final.groupby('brand')['brand'].transform('count')


    # In[227]:


    final = final[counts >= 2]


    # In[228]:


    final['brand'].value_counts()


    # In[229]:


    final = final.drop(columns=['webcam'])


    # In[230]:


    final.to_csv("../database/preprocessing/final.csv", encoding="utf-8-sig")


    # In[ ]:




