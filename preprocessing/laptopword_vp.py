#!/usr/bin/env python
# coding: utf-8

# In[68]:


import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import plotly.express as px
import seaborn as sns
import re


# In[69]:

def laptopworld_vp(file):

    df = pd.read_json(file)


    # In[70]:


    df


    # In[71]:


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


    # In[72]:


    df_new['name'] = df['name']


    # In[73]:


    df_new['name']


    # In[74]:


    df_new['brand'] = df['name'].str.extract(r'(Asus|Dell|Lenovo|HP|Acer|Apple|Acer|MSI|VAIO|LG|DELL|Chuwi|Lenovo|Microsoft|LENOVO|LENOVO|Dell|ASUS)')


    # In[75]:


    df_new['brand'].value_counts()


    # In[76]:


    df_new.loc[df_new['brand'].isin(['Asus', 'ASUS']), 'brand'] = 'Asus'


    # In[77]:


    for i in range(len(df['Bộ xử lý - CPU'])):
        if type(df['Bộ xử lý - CPU'][i]) == str:
            continue
        else:
            df.loc[i, 'Bộ xử lý - CPU'] = df.iloc[i, 22]


    # In[78]:


    df_new['chipset'] = df['Bộ xử lý - CPU'].str.extract(r'(Intel|AMD|Alder Lake|Apple)')


    # In[79]:


    df_new['chipset_gen'] = df['Bộ xử lý - CPU']


    # In[80]:


    df_new['screen_size'] = df['Màn hình - Monitor'].str.extract(r'(\d+(?:\.\d+)?)\s*inch')


    # In[81]:


    df_new['screen_revolution'] = df['Màn hình - Monitor'].str.extract(r'(\d+(?:\.\d+)?K|FHD|WUXGA|QHD|Full HD)')


    # In[82]:


    df_new['screen_full'] = df['Màn hình - Monitor'].str.extract(r'\((.*?)\)')


    # In[83]:


    df_new[['screen_width', 'screen_height']] = df_new['screen_full'].str.extract(r'(\d+)\s*[xX×]\s*(\d+)')


    # In[84]:


    df_new['screen_width'] = pd.to_numeric(df_new['screen_width'])
    df_new['screen_height'] = pd.to_numeric(df_new['screen_height'])


    # In[85]:


    df_new['ram'] = df['Bộ nhớ trong - Ram'].str.extract(r'(\d+)GB')


    # In[86]:


    df_new['storage_type']=df['Ổ đĩa cứng - HDD'].str.extract(r'(SSD|HDD)')


    # In[87]:


    df_new['storage_type'].value_counts()


    # In[88]:


    for i in range(len(df['Ổ đĩa cứng - HDD'])):
        if type(df['Ổ đĩa cứng - HDD'][i]) == str:
            continue
        else:
            df['Ổ đĩa cứng - HDD'][i] = df.iloc[:, 26][i]


    # In[89]:


    for i in range(len(df['Ổ đĩa cứng - HDD'])):
        if type(df['Ổ đĩa cứng - HDD'][i]) == str:
            continue
        else:
            df['Ổ đĩa cứng - HDD'][i] = df.iloc[:, 23][i]


    # In[90]:


    for i in range(len(df['Ổ đĩa cứng - HDD'])):
        if type(df['Ổ đĩa cứng - HDD'][i]) == str:
            continue
        else:
            df['Ổ đĩa cứng - HDD'][i] = df.iloc[:, 27][i]


    # In[91]:


    for i in range(len(df['Ổ đĩa cứng - HDD'])):
        if type(df['Ổ đĩa cứng - HDD'][i]) == str:
            continue
        else:
            df['Ổ đĩa cứng - HDD'][i] = df.iloc[:, 30][i]


    # In[92]:


    for i in range(len(df['Ổ đĩa cứng - HDD'])):
        if type(df['Ổ đĩa cứng - HDD'][i]) == str:
            continue
        else:
            df['Ổ đĩa cứng - HDD'][i] = df.iloc[:, 21][i]


    # In[93]:


    for i in range(len(df['Ổ đĩa cứng - HDD'])):
        if type(df['Ổ đĩa cứng - HDD'][i]) == str:
            continue
        else:
            df['Ổ đĩa cứng - HDD'][i] = df.iloc[:, 47][i]


    # In[94]:


    columns_info = [(col_name, col_number) for col_number, col_name in enumerate(df.columns)]


    # In[95]:


    size_info = df['Ổ đĩa cứng - HDD'].str.extract(r'(\d+)TB|(\d+)GB')


    # In[96]:


    df_new['storage'] = size_info.apply(lambda row: int(row[0]) * 1024 if pd.notna(row[0]) else (int(row[1]) if pd.notna(row[1]) else 0), axis=1)


    # In[97]:


    df_new['vga'] = df['Card đồ hoạ - Video'].str.lower().str.extract(r'(intel|amd|nvidia)')


    # In[98]:


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


    # In[99]:


    df_new['battery'] = df['Pin']
    df_new['battery'] = df_new['battery'].apply(get_battery_capacity)


    # In[100]:


    def get_number_from_string(s):
        if not isinstance(s, str):
            return None
        # Regular expression to match any floating point number
        pattern = r"[-+]?\d*\.\d+|\d+"
        # Find all matches of the pattern in the string
        matches = re.findall(pattern, s)
        # Convert the first match to a float and return
        return float(matches[0]) if matches else None


    # In[101]:


    get_number_from_string(" ")


    # In[102]:


    df_new['weight'] = df['Trọng lượng']


    # In[103]:


    df_new['weight'] = df_new['weight'].apply(get_number_from_string)


    # In[104]:


    df_new.loc[df_new['weight'] > 100, 'weight'] *= 0.001


    # In[105]:


    df_new['weight'].isna().sum()


    # In[106]:


    df_new['weight']


    # In[107]:


    df_new['price'] = df['gia goc'].str.replace(r'[^\d]', '', regex=True)
    df_new['price'] = pd.to_numeric(df_new['price'], errors='coerce')


    # In[108]:


    df_new['ram'] = pd.to_numeric(df_new['ram'].str.extract('(\d+)')[0])


    # In[109]:


    def get_ram_max(s):
        if not isinstance(s, str):
            return None
        match = re.search(r'(?:up to|tối đa)\s+(\d+)', s, re.IGNORECASE)
        if match:
            return int(match.group(1))
        else:
            return None


    # In[110]:


    df_new['ram_max'] = df['Bộ nhớ trong - Ram'].apply(get_ram_max)


    # In[111]:


    df_new['ram_max'] = df_new['ram_max'].fillna(df_new['ram'] * 1.5).infer_objects(copy=False)


    # In[112]:


    df_new['webcam'] = df['Webcam'].notnull().astype(int)


    # In[113]:


    df_new['webcam'].value_counts()


    # In[114]:


    for i in range(len(df['Hệ điều hành - Operation System'])):
        if type(df['Hệ điều hành - Operation System'][i]) == str:
            continue
        else:
            df.loc[i, 'Hệ điều hành - Operation System'] = df.iloc[i, 46]


    # In[115]:


    # for i in range(len(df['Hệ điều hành - Operation System'])):
    #     if type(df['Hệ điều hành - Operation System'][i]) != str:
    #         continue  
    #     if len(df['Hệ điều hành - Operation System'][i]) >=2:
    #         continue
    #     else:
    #         df.loc[i, 'Hệ điều hành - Operation System'] = df.loc[i, 'name']


    # In[116]:


    df_new['os'] = df['Hệ điều hành - Operation System'].str.extract(r'(Window. \d\d|Windows. \d\d|Win \d\d|Windows 11|Dos|Ubuntu|Mac OS|No OS|Fedora|NoOS|MAC|Windows® 11|Non OS|Window 11|Windows 11)')


    # In[117]:


    df_new['os'].value_counts()


    # In[118]:


    df_new = df_new.dropna(subset=['os'])


    # In[119]:


    df_new.loc[df_new['os'].isin(['Windows® 11', 'Window 11', 'Windows 11', 'Windows 11', 'Windows® 11']), 'os'] = 'Windows 11'
    df_new.loc[df_new['os'].isin(['Non OS', 'No OS']), 'os'] = 'NoOS'


    # In[120]:


    df_new.loc[df_new['os'].isin(['Windows 11', 'Windows 11', 'Windows® 11 ']), 'os'] = 'Windows 11'


    # In[121]:


    df_new.loc[df_new['os'].isin(['Windows® 11', 'Window 11', 'Windows 11', 'Windows 11', 'Windows® 11 ', 'Windows 11']), 'os'] = 'Windows 11'
    df_new.loc[df_new['os'].isin(['Non OS', 'No OS']), 'os'] = 'NoOS'


    # In[122]:


    df_new['os'].value_counts()


    # In[123]:


    mask = df.isin(['Windows® 11'])
    indices = df.loc[mask.any(axis=1)].index
    indices


    # In[242]:


    amd_df = df_new.loc[df_new['chipset'] == 'AMD']


    # In[243]:


    amd_df.loc[:, 'chipset_gen'] = amd_df['chipset_gen'].str.extract(r'(\d+)',expand=False)


    # In[244]:


    amd_df.loc[:, 'chipset_gen'] = 'Ryzen ' + amd_df['chipset_gen']


    # In[245]:


    intel_df = df_new.loc[df_new['chipset'] == 'Intel']


    # In[246]:


    intel_df.loc[:, 'chipset_gen'] = intel_df['chipset_gen'].str.extract(r'(i[3579]|Ultra [3579])',expand=False)


    # In[247]:


    intel_df['chipset_gen'].value_counts()


    # In[248]:


    df_new = pd.concat([amd_df, intel_df], ignore_index=True)


    # In[249]:


    df_new['chipset_gen'] = df_new['chipset_gen'].fillna('i5')


    # In[250]:


    mode_values = df_new.mode().iloc[0]
    df_new.fillna(mode_values, inplace=True)


    # In[251]:


    df_new.to_csv("../database/preprocessing/laptopworld_vp.csv", encoding="utf-8-sig")

