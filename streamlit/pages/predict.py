import pandas as pd
from sklearn.metrics import r2_score,mean_absolute_error, mean_squared_error, accuracy_score
import streamlit as st
import process_data

model = process_data.model

col1, col2, col3 = st.columns(3)

with col1:
    os = st.selectbox('OS', ['Win', 'No OS', 'Ubuntu', 'Mac OS', 'Dos', 'Fedora'])
    ram = st.number_input('RAM (GB)', min_value=0, max_value=1024, placeholder=0)
    vga = st.selectbox('VGA', ['intel', 'nvidia', 'amd'])
    battery = st.number_input('Battery (mAh)', min_value=0.0, max_value=2000.0, placeholder=0)
    weight = st.number_input('Weight (kg)', min_value=0.0, max_value=20.0, placeholder=0)
    webcam = st.checkbox('Webcam')
    st.write(webcam)

with col2:
    chipset = st.selectbox('Chipset', ['Intel', 'AMD', 'Apple'])
    chipset_gen = st.selectbox('Chipset_gen', ['i3', 'i5', 'i7', 'i9','Ryzen 3', 'Ryzen 5', 'Ryzen 7', 'Ryzen 9', 'M1', 'M2'])
    screen_size = st.number_input('Screen Size (inch)', min_value=0.0, max_value=50.0, placeholder=0)
    screen_width = st.number_input('Screen Width (px)', min_value=0, max_value=5000, placeholder=0)
    screen_height = st.number_input('Screen Height (px)', min_value=0, max_value=5000, placeholder=0)
    screen_revolution = st.selectbox('Screen Revolution', ['FHD', 'WUXGA', 'QHD', '2.8K', '2.2K', '3.5K', '3K', '2.5K', '2K', '4K'])
with col3:
    storage_type = st.selectbox('Storage Type', ['HDD', 'SSD'])
    storage = st.number_input('Storage (GB)', min_value=0, max_value=2000, placeholder=0)
    brand = st.selectbox('Brand', ['Dell', 'Lenovo', 'HP', 'Asus', 'Acer', 'MSI', 'LG', 'Apple', 'Gigabyte', 'VAIO', 'Microsoft', 'Chuwi'])
    ram_max = st.number_input('Max RAM (GB)', min_value=0, max_value=1024, placeholder=0)

if st.button('Model '):
    st.write("R2 score: ",  r2_score(process_data.y_test, process_data.model.predict(process_data.scaler.transform(process_data.X_test))))

if st.button('Predict'):
    webcam = 1 if webcam else 0
    data = {
        'os': [os],
        'ram': [ram],
        'vga': [vga],
        'battery': [battery],
        'weight': [weight],
        'webcam': [webcam],
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
    data = process_data.process_user_input(data, process_data.X_test)

    st.write('Predicted Price: ', model.predict(data))