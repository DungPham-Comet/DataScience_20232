import pandas as pd
from sklearn.metrics import r2_score, mean_absolute_error
import streamlit as st
from sklearn.tree import DecisionTreeRegressor

from untils.process_data import *

col1, col2, col3 = st.columns(3)

def get_keys(str):
    list = []
    for key in df[str].value_counts().keys():
        list.append(key)
    return list

with col1:
    os = st.selectbox('OS', get_keys('os'))
    ram = st.number_input('RAM (GB)', min_value=0, max_value=1024, placeholder=0)
    vga = st.selectbox('VGA', get_keys('vga'))
    battery = st.number_input('Battery (mAh)', min_value=0.0, max_value=2000.0, placeholder=0)
    weight = st.number_input('Weight (kg)', min_value=0.0, max_value=20.0, placeholder=0)


with col2:
    chipset = st.selectbox('Chipset', get_keys('chipset'))
    chipset_gen = st.selectbox('Chipset_gen', get_keys('chipset_gen'))
    screen_size = st.number_input('Screen Size (inch)', min_value=0.0, max_value=50.0, placeholder=0)
    screen_width = st.number_input('Screen Width (px)', min_value=0, max_value=5000, placeholder=0)
    screen_height = st.number_input('Screen Height (px)', min_value=0, max_value=5000, placeholder=0)
    screen_revolution = st.selectbox('Screen Revolution', get_keys('screen_revolution'))

with col3:
    storage_type = st.selectbox('Storage Type', ['HDD', 'SSD'])
    storage = st.number_input('Storage (GB)', min_value=0, max_value=2000, placeholder=0)
    brand = st.selectbox('Brand', get_keys('brand'))
    ram_max = st.number_input('Max RAM (GB)', min_value=0, max_value=1024, placeholder=0)

model_option = st.selectbox('Model', ['Random Forest', 'KNN', 'Decision Tree'])

model = None

if model_option == 'Random Forest':
    model = rf_model
    st.write('R2 score: ', r2_score(rf_y_test, rf_model.predict(
        scaler.transform(rf_X_test)))
    )
    st.write('MAE: ', mean_absolute_error(rf_y_test, rf_model.predict(
        scaler.transform(rf_X_test)))
    )

elif model_option == 'KNN':
    model = knn_model
    st.write('R2 score: ', r2_score(knn_y_test, knn_model.predict(
        scaler.transform(knn_X_test)))
    )
    st.write('MAE: ', mean_absolute_error(knn_y_test, knn_model.predict(
        scaler.transform(knn_X_test)))
    )

elif model_option == 'Decision Tree':
    model = tree_model
    st.write('R2 score: ', r2_score(tree_y_test, tree_model.predict(
        scaler.transform(tree_X_test)))
    )
    st.write('MAE: ', mean_absolute_error(tree_y_test, tree_model.predict(
        scaler.transform(tree_X_test)))
    )

@st.cache_resource
def best_model_rf():
    forest = RandomForestRegressor()
    param_grid = {
        'n_estimators': [50, 100, 200],
        'max_features': [6, 10, 50, 59, 55],
        'min_samples_split': [2, 4, 6, 8, 10]
    }

    grid_search = GridSearchCV(forest, param_grid, cv=10, return_train_score=True)
    grid_search.fit(X_train_scaled, y_train)
    best_forest = grid_search.best_estimator_

    return best_forest, X_test, y_test

@st.cache_resource
def best_model_knn():
    knn = KNeighborsRegressor()
    param_grid = {
        'n_neighbors': [5, 8, 10, 15, 20, 25, 30, 35, 40]
    }

    grid_search = GridSearchCV(knn, param_grid, cv=10, return_train_score=True)
    grid_search.fit(X_train_scaled, y_train)
    best_knn = grid_search.best_estimator_

    return best_knn, X_test, y_test

@st.cache_resource
def best_model_tree():
    tree = DecisionTreeRegressor()
    param_grid = {
        'max_depth': [5, 10, 15, 20, 25, 30, 35, 40],
        'min_samples_split': [2, 4, 6, 8, 10]
    }

    grid_search = GridSearchCV(tree, param_grid, cv=10, return_train_score=True)
    grid_search.fit(X_train_scaled, y_train)
    best_tree = grid_search.best_estimator_

    return best_tree, X_test, y_test

grid_search = st.toggle('Best model')

if grid_search:
    if model_option == 'Random Forest':
        model, rf_X_test, rf_y_test = best_model_rf()
        st.write('R2 score: ', r2_score(rf_y_test, model.predict(
            scaler.transform(rf_X_test)))
        )
        st.write('MAE: ', mean_absolute_error(rf_y_test, model.predict(
            scaler.transform(rf_X_test)))
        )
    elif model_option == 'KNN':
        model, knn_X_test, knn_y_test = best_model_knn()
        st.write('R2 score: ', r2_score(knn_y_test, model.predict(
            scaler.transform(knn_X_test)))
        )
        st.write('MAE: ', mean_absolute_error(knn_y_test, model.predict(
            scaler.transform(knn_X_test)))
        )
    elif model_option == 'Decision Tree':
        model, tree_X_test, tree_y_test = best_model_tree()
        st.write('R2 score: ', r2_score(tree_y_test, model.predict(
            scaler.transform(tree_X_test)))
        )
        st.write('MAE: ', mean_absolute_error(tree_y_test, model.predict(
            scaler.transform(tree_X_test)))
        )

if st.button('Predict'):
    data = {
        'os': [os],
        'ram': [ram],
        'vga': [vga],
        'battery': [battery],
        'weight': [weight],
        'chipset': [chipset],
        'chipset_gen': [chipset_gen],
        'screen_size': [screen_size],
        'screen_width': [screen_width],
        'screen_height': [screen_height],
        'screen_revolution': [screen_revolution],
        'storage_type': [storage_type],
        'storage': [storage],
        'brand': [brand],
        'ram_max': [ram_max]
    }

    data = pd.DataFrame(data)
    data = process_user_input(data, rf_X_test)

    st.write('Predicted Price: ', model.predict(data))