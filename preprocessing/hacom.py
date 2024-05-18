#!/usr/bin/env python
# coding: utf-8

# In[85]:


import numpy as np 
import pandas as pd 
from matplotlib import pyplot as plt
import plotly.express as px
import seaborn as sns
import re


# In[86]:

def hacom(files):

    df1 = pd.read_json(files[0])
    df2 = pd.read_json(files[1])
    df = pd.concat([df1, df2], ignore_index=True)


    # In[87]:


    df


    # In[88]:


    df.columns


    # In[89]:


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
    'screen_revolution',
    'battery',
    'webcam',
    'weight', 
    'price'
    ])


    # In[90]:


    df_new['name'] = df['name']


    # In[91]:


    df_new['brand'] = df['Hãng sản xuất']


    # In[92]:


    df_new['brand'].value_counts()


    # In[93]:


    df_new.loc[df_new['brand'].isin(['Asus', 'ASUS']), 'brand'] = 'Asus'


    # In[94]:


    df_new.loc[df_new['brand'].isin(['Acer', 'Acer ']), 'brand'] = 'Acer'


    # In[95]:


    df_new.loc[df_new['brand'].isin(['Dell', 'DELL']), 'brand'] = 'Dell'


    # In[96]:


    df_new.loc[df_new['brand'].isin(['Lenovo', 'LENOVO', 'LENOVO ', 'Lenovo ']), 'brand'] = 'Lenovo'


    # In[97]:


    df_new['brand'].value_counts()


    # In[98]:


    for i in range(len(df['VGA'])):
        if type(df['VGA'][i]) == str:
            continue
        else:
            df.loc[i, 'VGA'] = df.iloc[i, 68]


    # In[99]:


    df_new['vga'] = df["VGA"].str.lower().str.extract(r'(intel|amd|nvidia|apple)')


    # In[100]:


    df_new['vga']


    # In[101]:


    df_new['vga'].value_counts()


    # In[102]:


    df_new['price'] = df['giá gốc'].str.replace("₫", "")


    # In[103]:


    df_new['price']


    # In[104]:


    df_new['price'] = df_new['price'].str.replace(".", "")


    # In[105]:


    df_new['price'].isna().sum()


    # In[106]:


    df_new = df_new.dropna(subset=['price'])


    # In[107]:


    df_new['price'].isna().sum()


    # In[108]:


    df_new['chipset'] = df['Bộ vi xử lý'].str.extract(r'(Intel|AMD|Apple)')


    # In[109]:


    df_new['chipset'].value_counts()


    # In[110]:


    for i in range(len(df['Bộ nhớ trong'])):
        if type(df['Bộ nhớ trong'][i]) == str:
            continue
        else:
            df.loc[i, 'Bộ nhớ trong'] = df.iloc[i, 99]


    # In[111]:


    for i in range(len(df['Bộ nhớ trong'])):
        if type(df['Bộ nhớ trong'][i]) == str:
            continue
        else:
            df.loc[i, 'Bộ nhớ trong'] = df.iloc[i, 52]


    # In[112]:


    for i in range(len(df['Bộ nhớ trong'])):
        if type(df['Bộ nhớ trong'][i]) == str:
            continue
        else:
            df.loc[i, 'Bộ nhớ trong'] = df.iloc[i, 65]


    # In[113]:


    df_new['ram'] = df["Bộ nhớ trong"].str.extract(r'(\d*.GB|\d*.G)')
    df_new['ram'] = df_new['ram'].str.replace(' ', '')
    df_new['ram'] = df_new['ram'].str.replace('G', 'GB')
    df_new['ram'] = df_new['ram'].str.replace('GBB', 'GB')
    df_new['ram'] = df_new['ram'].str.replace('GB', '')


    # In[114]:


    for i in range(len(df['Dung lượng tối đa'])):
        if type(df['Dung lượng tối đa'][i]) == str:
            continue
        else:
            df.loc[i, 'Dung lượng tối đa'] = df.iloc[i, 54]


    # In[115]:


    for i in range(len(df['Dung lượng tối đa'])):
        if type(df['Dung lượng tối đa'][i]) == str:
            continue
        else:
            df.loc[i, 'Dung lượng tối đa'] = df.iloc[i, 102]


    # In[116]:


    for i in range(len(df['Dung lượng tối đa'])):
        if type(df['Dung lượng tối đa'][i]) == str:
            continue
        else:
            df.loc[i, 'Dung lượng tối đa'] = df.iloc[i, 67]


    # In[117]:


    df.iloc[:, 67].value_counts()


    # In[118]:


    df_new['ram_max'] = df['Dung lượng tối đa'].str.extract(r'(\d+)GB*')


    # In[119]:


    df_new['ram_max'][71]


    # In[120]:


    for i in range(len(df['Ổ cứng'])):
        if type(df['Ổ cứng'][i]) == str:
            continue
        else:
            df.loc[i, 'Ổ cứng'] = df.iloc[i, 69]


    # In[121]:


    for i in range(len(df['Ổ cứng'])):
        if type(df['Ổ cứng'][i]) == str:
            continue
        else:
            df.loc[i, 'Ổ cứng'] = df.iloc[i, 103]


    # In[122]:


    df.iloc[:, 83].value_counts()


    # In[123]:


    df_new['storage_type'] = df['Ổ cứng'].str.extract(r'(SSD|HDD)')


    # In[124]:


    size_info = df['Ổ cứng'].str.extract(r'(\d+)TB|(\d+)GB')


    # In[125]:


    df_new['storage'] = size_info.apply(lambda row: int(row[0]) * 1024 if pd.notna(row[0]) else (int(row[1]) if pd.notna(row[1]) else 512), axis=1)


    # In[126]:


    for i in range(len(df['Hệ điều hành'])):
        if type(df['Hệ điều hành'][i]) == str:
            continue
        else:
            df.loc[i, 'Hệ điều hành'] = df.iloc[i, 83]


    # In[127]:


    df_new['os'] = df["Hệ điều hành"].str.extract(r'(Window.\d\d|Window. \d\d|Win \d\d|Dos|Ubuntu|Mac OS|No OS|Fedora)')


    # In[128]:


    df_new['os'].value_counts()


    # In[129]:


    df_new.loc[df_new['os'].isin(['Windows 11', 'Win 11', 'Windows11', 'Window 11']), 'os'] = 'Windows 11'
    df_new.loc[df_new['os'].isin(['Windows10', 'Win 10']), 'os'] = 'Windows 10'


    # In[130]:


    df_new['os'].value_counts()


    # In[131]:


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


    # In[132]:


    df_new['battery'] = df['Pin']
    df_new['battery'] = df_new['battery'].apply(get_battery_capacity)


    # In[133]:


    df_new['screen_size'] = df['Màn hình'].str.extract(r'(\d*\.*\d+-inch|\d*\.*\d+ *inch|\d*\.*\d+-Inch|\d*\.*\d+ *Inch|\d*\.*\d+")')
    df_new['screen_revolution'] = df['Màn hình'].str.extract(r'(FHD|2.5K|4K|WUXGA|QHD|Full HD)')
    df_new['screen_pixels'] = df['Màn hình'].str.extract(r'(\d+ *x *\d+|\d+ *\* *\d+|\d+ *X *\d+)')

    df_new['screen_size'] = df_new['screen_size'].str.replace('-inch', '')
    df_new['screen_size'] = df_new['screen_size'].str.replace('inch', '')
    df_new['screen_size'] = df_new['screen_size'].str.replace('Inch', '')
    df_new['screen_size'] = df_new['screen_size'].str.replace('"', '')
    df_new['screen_size'] = df_new['screen_size'].str.replace(' ', '')
    df_new['screen_revolution'] = df_new['screen_revolution'].str.replace('Full HD', 'FHD')
    df_new['screen_pixels'] = df_new['screen_pixels'].str.replace(' ', '')
    df_new['screen_pixels'] = df_new['screen_pixels'].str.replace('*', 'x')
    df_new['screen_pixels'] = df_new['screen_pixels'].str.replace('X', 'x')


    # In[134]:


    df_new[['screen_width', 'screen_height']] = df_new['screen_pixels'].str.extract(r'(\d+)\s*[xX×]\s*(\d+)')


    # In[135]:


    df_new['weight'] = df['Cân nặng'].str.extract(r'(\d*\.*\d* *kg|\d*\.*\d* *Kg)')
    df_new['weight'] = df_new['weight'].str.replace("Kg", '')
    df_new['weight'] = df_new['weight'].str.replace("kg", '')


    # In[136]:


    df_new.loc[df_new['weight'] == 72, 'weight'] = 1.72


    # In[137]:


    df_new['webcam'] = df['Webcam'].notnull().astype(int)


    # In[138]:


    df_new['chipset_gen'] = df['Bộ vi xử lý'].str.extract(r'(I\d.\w+|i\d.\w+|AMD.* *\d* *\w*|Apple \w*)')


    # In[139]:


    df_new['chipset_gen']


    # In[140]:


    amd_df = df_new.loc[df_new['chipset'] == 'AMD']


    # In[141]:


    amd_df.loc[:, 'chipset_gen'] = amd_df['chipset_gen'].str.extract(r'(\d+)', expand=False)


    # In[142]:


    amd_df.loc[:, 'chipset_gen'] = 'Ryzen ' + amd_df['chipset_gen']


    # In[143]:


    intel_df = df_new.loc[df_new['chipset'] == 'Intel']


    # In[144]:


    intel_df.loc[:, 'chipset_gen'] = intel_df.loc[:, 'chipset_gen'].str.extract(r'(i[3579]|Ultra [3579])', expand=False)


    # In[145]:


    apple_df = df_new.loc[df_new['chipset'] == 'Apple']


    # In[146]:


    apple_df['chipset_gen'] = apple_df['chipset_gen'].str.extract(r'(M[123])', expand=False)


    # In[147]:


    df_new = pd.concat([amd_df, intel_df, apple_df], ignore_index=True)


    # In[148]:


    mode_values = df_new.mode().iloc[0]
    df_new.fillna(mode_values, inplace=True)


    # In[149]:


    df_new.to_csv("../database/preprocessing/hacom.csv", encoding="utf-8-sig")


    # In[ ]:




