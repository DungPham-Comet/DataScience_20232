import pandas as pd
import streamlit as st
from bokeh.plotting import figure
import process_data
import plotly.express as px

df = pd.read_csv('data.csv')
df.dropna()

def price():
    # Price distribution
    fig = px.histogram(df, x='price', title='Biểu đồ phân bố giá laptop')
    st.plotly_chart(fig)

def brand():
    # Brand count
    brand_counts = df['brand'].value_counts().reset_index()
    brand_counts.columns = ['brand', 'count']

    fig = px.bar(brand_counts, x='brand', y='count', title='Số lượng các hãng laptop',
                 labels={'brand': 'Hãng', 'count': 'Số lượng'}, text='count', width=800, height=600)

    fig.update_traces(textposition='outside')

    st.plotly_chart(fig)

def ram():
    # Price vs RAM

    fig = px.scatter(df, x='ram', y='price', title='Mối liên hệ giữa RAM và giá cả',
                     labels={'ram': 'RAM', 'price': 'Giá cả'})

    st.plotly_chart(fig)

def weight():
    # Price vs Weight
    fig = px.scatter(df, x='weight', y='price', title='Mối liên hệ giữa Weight và giá cả',
                     labels={'weight': 'Weight', 'price': 'Giá cả'})

    st.plotly_chart(fig)

def storage():
    # Storage vs Price
    fig = px.scatter(df, x='storage', y='price', title='Mối liên hệ giữa Storage và giá cả',
                     labels={'storage': 'Storage', 'price': 'Giá cả'})

    st.plotly_chart(fig)


options = st.multiselect(
    'Chọn features muốn phân tích',
    ['price', 'brand', 'weight', 'ram', 'storage']
)

for option in options:
    if (option == 'price'):
        price()
    elif (option == 'brand'):
        brand()
    elif (option == 'ram'):
        ram()
    elif (option == 'storage'):
        storage()
    elif (option == 'weight'):
        weight()
