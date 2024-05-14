
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import plotly.express as px
import seaborn as sns
import re


# In[189]:

def laptopworld_vp(file):

    df = pd.read_json(file)


    # In[190]:


    df


    # In[191]:


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


    # In[192]:


    df_new['name'] = df['name']


    # In[193]:


    df_new['name']


    # In[194]:


    df_new['brand'] = df['name'].str.extract(r'(Asus|Dell|Lenovo|HP|Acer|Apple|Acer|MSI|VAIO|LG|DELL|Chuwi|Lenovo|Microsoft|LENOVO|LENOVO|Dell|ASUS)')


    # In[195]:


    df_new['brand'].value_counts()


    # In[196]:


    df_new.loc[df_new['brand'].isin(['Asus', 'ASUS']), 'brand'] = 'Asus'


    # In[197]:


    for i in range(len(df['Bộ xử lý - CPU'])):
        if type(df['Bộ xử lý - CPU'][i]) == str:
            continue
        else:
            df.loc[i, 'Bộ xử lý - CPU'] = df.iloc[i, 22]


    # In[198]:


    df_new['chipset'] = df['Bộ xử lý - CPU'].str.extract(r'(Intel|AMD|Alder Lake|Apple)')


    # In[199]:


    df_new['chipset_gen'] = df['Bộ xử lý - CPU']


    # In[200]:


    df_new['screen_size'] = df['Màn hình - Monitor'].str.extract(r'(\d+(?:\.\d+)?)\s*inch')


    # In[201]:


    df_new['screen_revolution'] = df['Màn hình - Monitor'].str.extract(r'(\d+(?:\.\d+)?K|FHD|WUXGA|QHD|Full HD)')


    # In[202]:


    df_new['screen_full'] = df['Màn hình - Monitor'].str.extract(r'\((.*?)\)')


    # In[203]:


    df_new[['screen_width', 'screen_height']] = df_new['screen_full'].str.extract(r'(\d+)\s*[xX×]\s*(\d+)')


    # In[204]:


    df_new['screen_width'] = pd.to_numeric(df_new['screen_width'])
    df_new['screen_height'] = pd.to_numeric(df_new['screen_height'])


    # In[205]:


    df_new['ram'] = df['Bộ nhớ trong - Ram'].str.extract(r'(\d+)GB')


    # In[206]:


    df_new['storage_type']=df['Ổ đĩa cứng - HDD'].str.extract(r'(SSD|HDD)')


    # In[207]:


    df_new['storage_type'].value_counts()


    # In[208]:


    for i in range(len(df['Ổ đĩa cứng - HDD'])):
        if type(df['Ổ đĩa cứng - HDD'][i]) == str:
            continue
        else:
            df['Ổ đĩa cứng - HDD'][i] = df.iloc[:, 26][i]


    # In[209]:


    for i in range(len(df['Ổ đĩa cứng - HDD'])):
        if type(df['Ổ đĩa cứng - HDD'][i]) == str:
            continue
        else:
            df['Ổ đĩa cứng - HDD'][i] = df.iloc[:, 23][i]


    # In[210]:


    for i in range(len(df['Ổ đĩa cứng - HDD'])):
        if type(df['Ổ đĩa cứng - HDD'][i]) == str:
            continue
        else:
            df['Ổ đĩa cứng - HDD'][i] = df.iloc[:, 27][i]


    # In[211]:


    for i in range(len(df['Ổ đĩa cứng - HDD'])):
        if type(df['Ổ đĩa cứng - HDD'][i]) == str:
            continue
        else:
            df['Ổ đĩa cứng - HDD'][i] = df.iloc[:, 30][i]


    # In[212]:


    for i in range(len(df['Ổ đĩa cứng - HDD'])):
        if type(df['Ổ đĩa cứng - HDD'][i]) == str:
            continue
        else:
            df['Ổ đĩa cứng - HDD'][i] = df.iloc[:, 21][i]


    # In[213]:


    for i in range(len(df['Ổ đĩa cứng - HDD'])):
        if type(df['Ổ đĩa cứng - HDD'][i]) == str:
            continue
        else:
            df['Ổ đĩa cứng - HDD'][i] = df.iloc[:, 47][i]


    # In[214]:


    columns_info = [(col_name, col_number) for col_number, col_name in enumerate(df.columns)]

    # Print the list of columns and their corresponding column numbers
    for col_name, col_number in columns_info:
        print(f"Column Name: {col_name}, Column Number: {col_number}")


    # In[215]:


    size_info = df['Ổ đĩa cứng - HDD'].str.extract(r'(\d+)TB|(\d+)GB')


    # In[216]:


    df_new['storage'] = size_info.apply(lambda row: int(row[0]) * 1024 if pd.notna(row[0]) else (int(row[1]) if pd.notna(row[1]) else 0), axis=1)


    # In[217]:


    df_new['vga'] = df['Card đồ hoạ - Video'].str.lower().str.extract(r'(intel|amd|nvidia)')


    # In[218]:


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


    # In[219]:


    df_new['battery'] = df['Pin']
    df_new['battery'] = df_new['battery'].apply(get_battery_capacity)


    # In[220]:


    def get_number_from_string(s):
        if not isinstance(s, str):
            return None
        # Regular expression to match any floating point number
        pattern = r"[-+]?\d*\.\d+|\d+"
        # Find all matches of the pattern in the string
        matches = re.findall(pattern, s)
        # Convert the first match to a float and return
        return float(matches[0]) if matches else None


    # In[221]:


    get_number_from_string(" ")


    # In[222]:


    df_new['weight'] = df['Trọng lượng']


    # In[223]:


    df_new['weight'] = df_new['weight'].apply(get_number_from_string)


    # In[224]:


    df_new.loc[df_new['weight'] > 100, 'weight'] *= 0.001


    # In[225]:


    df_new['weight'].isna().sum()


    # In[226]:


    df_new['weight']


    # In[227]:


    df_new['price'] = df['gia goc'].str.replace(r'[^\d]', '', regex=True)
    df_new['price'] = pd.to_numeric(df_new['price'], errors='coerce')


    # In[228]:


    df_new['ram'] = pd.to_numeric(df_new['ram'].str.extract('(\d+)')[0])


    # In[229]:


    def get_ram_max(s):
        if not isinstance(s, str):
            return None
        match = re.search(r'(?:up to|tối đa)\s+(\d+)', s, re.IGNORECASE)
        if match:
            return int(match.group(1))
        else:
            return None


    # In[230]:


    df_new['ram_max'] = df['Bộ nhớ trong - Ram'].apply(get_ram_max)


    # In[231]:


    df_new['ram_max'] = df_new['ram_max'].fillna(df_new['ram'] * 1.5).infer_objects(copy=False)


    # In[232]:


    df_new['webcam'] = df['Webcam'].notnull().astype(int)


    # In[233]:


    df_new['webcam'].value_counts()


    # In[234]:


    for i in range(len(df['Hệ điều hành - Operation System'])):
        if type(df['Hệ điều hành - Operation System'][i]) == str:
            continue
        else:
            df.loc[i, 'Hệ điều hành - Operation System'] = df.iloc[i, 30]


    # In[235]:


    for i in range(len(df['Hệ điều hành - Operation System'])):
        if type(df['Hệ điều hành - Operation System'][i]) != str:
            continue  
        if len(df['Hệ điều hành - Operation System'][i]) >=2:
            continue
        else:
            df.loc[i, 'Hệ điều hành - Operation System'] = df.loc[i, 'name']


    # In[236]:


    df_new['os'] = df['Hệ điều hành - Operation System'].str.extract(r'(Window. \d\d|Windows. \d\d|Win \d\d|Windows 11|Dos|Ubuntu|Mac OS|No OS|Fedora|NoOS|MAC|Windows® 11|Non OS|Window 11|Windows 11)')


    # In[237]:


    df_new['os'].value_counts()


    # In[238]:


    df_new = df_new.dropna(subset=['os'])


    # In[239]:


    df_new.loc[df_new['os'].isin(['Windows® 11', 'Window 11', 'Windows 11', 'Windows 11', 'Windows® 11']), 'os'] = 'Windows 11'
    df_new.loc[df_new['os'].isin(['Non OS', 'No OS']), 'os'] = 'NoOS'


    # In[240]:


    df_new.loc[df_new['os'].isin(['Windows 11', 'Windows 11', 'Windows® 11 ']), 'os'] = 'Windows 11'


    # In[241]:


    df_new['os'].value_counts()


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


    df_new.to_csv("laptopworld_vp.csv", encoding="utf-8-sig")

