import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import os
import json


# current_dir = os.path.dirname(__file__)
# file_path = os.path.join(current_dir, '', 'laptopCrawler', 'laptopCrawler', 'DataCrawl', 'test.json')
#
# absolute_path = os.path.abspath(file_path)
# print(f"Đường dẫn tuyệt đối: {absolute_path}")
#;
#
# with open(absolute_path, 'r', encoding='utf-8') as file:
#     data = json.load(file)

if st.button('Crawl data'):
    #os.system('cd laptopCrawler && python aps_crawl.py')
    os.system('cd database && python process_filename.py')