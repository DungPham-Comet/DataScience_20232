#!/usr/bin/env python
# coding: utf-8

# In[56]:


import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import plotly.express as px
import seaborn as sns
import re


# In[57]:

def laptopworld_gm(file):

    df = pd.read_json(file)


    # In[58]:


    df


    # In[59]:


    df_new = pd.DataFrame(columns=[
    'name',
    'brand',
    'chipset',
    'chipset_gen',
    'ram', 
    'ram_max', 
    'vga',
    'storage_type',
    'storage', 
    'os',
    'screen_size',
    'screen_width',
    'screen_height',
    'screen_revolution',
    'battery',
    'webcam',
    'weight', 
    'price'
    ])


    # In[60]:


    df_new['name'] = df['name']


    # In[61]:


    df_new['name']


    # In[62]:


    df_new['brand'] = df['name'].str.extract(r'(Asus|Dell|Lenovo|HP|Acer|Apple|Acer|MSI|VAIO|LG|DELL|Chuwi|Lenovo|Microsoft|LENOVO|LENOVO|Dell|ASUS)')


    # In[63]:


    df_new['brand'].value_counts()


    # In[64]:


    for i in range(len(df['Bộ xử lý - CPU'])):
        if type(df.loc[i, 'Bộ xử lý - CPU']) == str:
            continue
        else:
            df.loc[i, 'Bộ xử lý - CPU'] = df.iloc[:, 22][i]


    # In[65]:


    df_new['chipset'] = df['Bộ xử lý - CPU'].str.extract(r'(Intel|AMD|Alder Lake|Apple)')


    # In[66]:


    df_new['chipset_gen'] = df['Bộ xử lý - CPU']


    # In[67]:


    df_new['screen_size'] = df['Màn hình - Monitor'].str.extract(r'(\d+(?:\.\d+)?)\s*inch')


    # In[68]:


    df_new['screen_revolution'] = df['Màn hình - Monitor'].str.extract(r'(\d+(?:\.\d+)?K|FHD|WUXGA|QHD|Full HD)')


    # In[69]:


    df_new['screen_full'] = df['Màn hình - Monitor'].str.extract(r'\((.*?)\)')


    # In[70]:


    df_new[['screen_width', 'screen_height']] = df_new['screen_full'].str.extract(r'(\d+)\s*[xX×]\s*(\d+)')


    # In[71]:


    df_new['screen_width'] = pd.to_numeric(df_new['screen_width'])
    df_new['screen_height'] = pd.to_numeric(df_new['screen_height'])


    # In[72]:


    df_new['ram'] = df['Bộ nhớ trong - Ram'].str.extract(r'(\d+)GB')


    # In[73]:


    df_new['storage_type']=df['Ổ đĩa cứng - HDD'].str.extract(r'(SSD|HDD)')


    # In[74]:


    df_new['storage_type'].value_counts()


    # In[75]:


    for i in range(len(df['Ổ đĩa cứng - HDD'])):
        if type(df.loc[i,'Ổ đĩa cứng - HDD']) == str:
            continue
        else:
            df.loc[i,'Ổ đĩa cứng - HDD'] = df['Ổ cứng'][i]


    # In[76]:


    for i in range(len(df['Ổ đĩa cứng - HDD'])):
        if type(df.loc[i,'Ổ đĩa cứng - HDD']) == str:
            continue
        else:
            df.loc[i,'Ổ đĩa cứng - HDD'] = df.iloc[:, 21][i]


    # In[77]:


    size_info = df['Ổ đĩa cứng - HDD'].str.extract(r'(\d+)TB|(\d+)GB')


    # In[78]:


    df_new['storage'] = size_info.apply(lambda row: int(row[0]) * 1024 if pd.notna(row[0]) else (int(row[1]) if pd.notna(row[1]) else 0), axis=1)


    # In[79]:


    df_new['vga'] = df['Card đồ hoạ - Video'].str.lower().str.extract(r'(intel|amd|nvidia)')


    # In[80]:


    def get_battery_capacity(string):
        # Check if the input string is None
        if not isinstance(string, str):
            return None
        
        # Regular expression to match battery capacity
        pattern = r'(\d+(\.\d+)?)\s*Wh?'
        
        # Search for the pattern in the string
        match = re.search(pattern, string)
        
        if match:
            # Extract the matched capacity
            capacity = float(match.group(1))
            return capacity
        else:
            return None

    # Test cases
    print(get_battery_capacity("3Cell 52.5WHrs"))  # Output: 52.5
    print(get_battery_capacity("4Cell 80WH"))     # Output: 80
    print(get_battery_capacity("4Cell, 90Wh"))    # Output: 90


    # In[81]:


    df_new['battery'] = df['Pin']
    df_new['battery'] = df_new['battery'].apply(get_battery_capacity)


    # In[82]:


    df_new['battery'].isna().sum()


    # In[83]:


    df_new['battery'].index[df_new['battery'].isna()].tolist()


    # In[84]:


    def get_number_from_string(s):
        if not isinstance(s, str):
            return None
        # Regular expression to match any floating point number
        pattern = r"[-+]?\d*\.\d+|\d+"
        # Find all matches of the pattern in the string
        matches = re.findall(pattern, s)
        # Convert the first match to a float and return
        return float(matches[0]) if matches else None


    # In[85]:


    get_number_from_string(" ")


    # In[86]:


    df_new['weight'] = df['Trọng lượng']


    # In[87]:


    df_new['weight'] = df_new['weight'].apply(get_number_from_string)


    # In[88]:


    df_new['weight'].isna().sum()


    # In[89]:


    df_new['weight'].value_counts()


    # In[90]:


    df_new.loc[df_new['weight'] > 100, 'weight'] *= 0.001


    # In[91]:


    df_new['price'] = df['gia_chinh_hang'].str.replace(r'[^\d]', '', regex=True)
    df_new['price'] = pd.to_numeric(df_new['price'], errors='coerce')


    # In[92]:


    df_new['ram'] = pd.to_numeric(df_new['ram'].str.extract('(\d+)')[0])


    # In[93]:


    def get_ram_max(s):
        if not isinstance(s, str):
            return None
        match = re.search(r'(?:up to|tối đa)\s+(\d+)', s, re.IGNORECASE)
        if match:
            return int(match.group(1))
        else:
            return None


    # In[94]:


    df_new['ram_max'] = df['Bộ nhớ trong - Ram'].apply(get_ram_max)


    # In[95]:


    df_new['ram_max'] = df_new['ram_max'].fillna(df_new['ram'] * 1.5).infer_objects(copy=False)


    # In[96]:


    df_new['webcam'] = df['Webcam'].notnull().astype(int)


    # In[97]:


    df_new['webcam'].value_counts()


    # In[98]:


    for i in range(len(df['Hệ điều hành - Operation System'])):
        if type(df.loc[i,'Hệ điều hành - Operation System']) == str:
            continue
        else:
            df.loc[i,'Hệ điều hành - Operation System'] = df.iloc[:, 30][i]


    # In[99]:


    for i in range(len(df['Hệ điều hành - Operation System'])):
        if type(df['Hệ điều hành - Operation System'][i]) != str:
            continue  
        if len(df['Hệ điều hành - Operation System'][i]) >=2:
            continue
        else:
            df['Hệ điều hành - Operation System'][i] = df['name'][i]


    # In[100]:


    df_new['os'] = df['Hệ điều hành - Operation System'].str.extract(r'(Window. \d\d|Windows. \d\d|Win \d\d|Windows 11|Dos|Ubuntu|Mac OS|No OS|Fedora|NoOS|MAC|Windows® 11|Non OS|Window 11|Windows 11)')


    # In[101]:


    df_new['os'].value_counts()


    # In[102]:


    df_new = df_new.dropna(subset=['os'])


    # In[103]:


    df_new.loc[df_new['os'].isin(['Windows® 11', 'Window 11', 'Windows 11', 'Windows 11', 'Windows® 11']), 'os'] = 'Windows 11'
    df_new.loc[df_new['os'].isin(['Non OS', 'No OS']), 'os'] = 'NoOS'


    # In[104]:


    df_new['os'].value_counts()


    # In[105]:


    amd_df = df_new.loc[df_new['chipset'] == 'AMD']


    # In[106]:


    amd_df.loc[:, 'chipset_gen'] = amd_df['chipset_gen'].str.extract(r'(\d+)',expand=False)


    # In[107]:


    amd_df.loc[:, 'chipset_gen'] = 'Ryzen ' + amd_df['chipset_gen']


    # In[108]:


    intel_df = df_new.loc[df_new['chipset'] == 'Intel']


    # In[109]:


    intel_df.loc[:, 'chipset_gen'] = intel_df['chipset_gen'].str.extract(r'(i[3579]|Ultra [3579])',expand=False)


    # In[110]:


    df_new = pd.concat([amd_df, intel_df], ignore_index=True)


    # In[111]:


    df_new['chipset_gen'] = df_new['chipset_gen'].fillna('i7')


    # In[112]:


    mode_values = df_new.mode().iloc[0]
    df_new.fillna(mode_values, inplace=True)


    # In[113]:


    df_new.to_csv("laptopworld_gaming.csv", encoding="utf-8-sig")


    # In[ ]:




