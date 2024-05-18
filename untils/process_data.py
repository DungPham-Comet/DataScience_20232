import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score,mean_absolute_error, mean_squared_error, accuracy_score
import streamlit as st

df = pd.read_csv('database/preprocessing/final.csv')
@st.cache_data
def process_data(df):
    df = df.dropna()
    df = df.drop('Unnamed: 0', axis=1)
    df = df.drop('Unnamed: 0.1', axis=1)
    df = df.drop('name', axis=1)

    df['chipset'] = df['chipset'].apply(lambda x: 'chipset_' + x)
    df['os'] = df['os'].apply(lambda x: 'os_' + x)
    df['vga'] = df['vga'].apply(lambda x: 'vga_' + x)
    df['chipset_gen'] = df['chipset_gen'].apply(lambda x: 'chipset_gen_' + x)
    df['screen_revolution'] = df['screen_revolution'].apply(lambda x: 'screen_revolution_' + x)
    df['storage_type'] = df['storage_type'].apply(lambda x: 'storage_type_' + x)
    df['brand'] = df['brand'].apply(lambda x: 'brand_' + x)

    df['chipset'] = df['chipset'].apply(lambda x: x.casefold())
    df['os'] = df['os'].apply(lambda x: x.casefold())
    df['vga'] = df['vga'].apply(lambda x: x.casefold())
    df['chipset_gen'] = df['chipset_gen'].apply(lambda x: x.casefold())
    df['screen_revolution'] = df['screen_revolution'].apply(lambda x: x.casefold())
    df['storage_type'] = df['storage_type'].apply(lambda x: x.casefold())
    df['brand'] = df['brand'].apply(lambda x: x.casefold())

    df = df.join(pd.get_dummies(df.brand, dtype=int))
    df = df.join(pd.get_dummies(df.chipset, dtype=int))
    df = df.join(pd.get_dummies(df.chipset_gen, dtype=int))
    df = df.join(pd.get_dummies(df.vga, dtype=int))
    df = df.join(pd.get_dummies(df.storage_type, dtype=int))
    df = df.join(pd.get_dummies(df.os, dtype=int))
    df = df.join(pd.get_dummies(df.screen_revolution, dtype=int))

    df = df.drop(columns=['brand', 'chipset', 'chipset_gen', 'vga', 'storage_type', 'os', 'screen_revolution'])

    return df

new_df = process_data(df)

scaler = StandardScaler()
X, y = new_df.drop('price', axis=1), new_df['price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15, random_state=42)
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

@st.cache_resource
def train_model_rf():
    forest = RandomForestRegressor()
    forest.fit(X_train_scaled, y_train)

    return forest, X_test, y_test
@st.cache_resource
def train_model_knn():
    knn = KNeighborsRegressor()
    knn.fit(X_train_scaled, y_train)

    return knn, X_test, y_test
@st.cache_resource
def train_model_lr():
    lr = LinearRegression()
    lr.fit(X_train_scaled, y_train)

    return lr, X_test, y_test

rf_model, rf_X_test, rf_y_test = train_model_rf()
knn_model, knn_X_test, knn_y_test = train_model_knn()
lr_model, lr_X_test, lr_y_test = train_model_lr()

@st.cache_data
def process_user_input(user_input, X_test):
    user_input['chipset'] = user_input['chipset'].apply(lambda x: 'chipset_' + x)
    user_input['os'] = user_input['os'].apply(lambda x: 'os_' + x)
    user_input['vga'] = user_input['vga'].apply(lambda x: 'vga_' + x)
    user_input['chipset_gen'] = user_input['chipset_gen'].apply(lambda x: 'chipset_gen_' + x)
    user_input['screen_revolution'] = user_input['screen_revolution'].apply(lambda x: 'screen_revolution_' + x)
    user_input['storage_type'] = user_input['storage_type'].apply(lambda x: 'storage_type_' + x)
    user_input['brand'] = user_input['brand'].apply(lambda x: 'brand_' + x)

    user_input['chipset'] = user_input['chipset'].apply(lambda x: x.casefold())
    user_input['os'] = user_input['os'].apply(lambda x: x.casefold())
    user_input['vga'] = user_input['vga'].apply(lambda x: x.casefold())
    user_input['chipset_gen'] = user_input['chipset_gen'].apply(lambda x: x.casefold())
    user_input['screen_revolution'] = user_input['screen_revolution'].apply(lambda x: x.casefold())
    user_input['storage_type'] = user_input['storage_type'].apply(lambda x: x.casefold())
    user_input['brand'] = user_input['brand'].apply(lambda x: x.casefold())

    categorical_columns = ['os', 'vga', 'chipset', 'chipset_gen', 'screen_revolution', 'storage_type', 'brand']
    new_data_dummies = pd.get_dummies(user_input, columns=categorical_columns)

    df_columns = X_test.columns
    new_data_transformed = pd.DataFrame(0, index=[0], columns=df_columns)

    for col in new_data_dummies.columns:
        if col in new_data_transformed.columns:
            new_data_transformed[col] = new_data_dummies[col]

    numeric_columns = ['ram', 'battery', 'weight', 'screen_size', 'screen_width', 'screen_height', 'storage',
                       'ram_max']
    for col in numeric_columns:
        if col in new_data_transformed.columns:
            new_data_transformed[col] = user_input[col]

    input_scaled = scaler.transform(new_data_transformed)

    return input_scaled



