import pickle
import streamlit as st

# membaca model
kerusakan_model = pickle.load(open('model_kerusakan_lr.sav', 'rb'))

# Judul web
st.title('Aplikasi Prediksi Kerusakan Mesin')

# Ide membagi kolom
col1, col2, col3 = st.columns(3)

with col1 :
    footfall = st.number_input('input nilai benda yang melewati mesin')

with col1 :
    tempMode = st.number_input('input nilai mode suhu mesin')

with col1 :
    AQ = st.number_input('input nilai kualitas udara')

with col2 :
    USS = st.number_input('input nilai sensor ultrasonik')

with col2 :
    CS = st.number_input('input nilai penggunaan arus listrik')

with col2 :
    VOC = st.number_input('input nilai senyawa volatil')

with col3 :
    RP = st.number_input('input nilai putaran permenit')

with col3 :
    IP = st.number_input('input nilai tekanan masukan mesin')

with col3 :
    Temperature = st.number_input('input nilai suhu pengoperasian mesin')

# code untuk prediksi
fail_diagnosis = ''

# membuat tombol prediksi
if st.button('Test Prediksi Kerusakan'):
    fail_prediction = kerusakan_model.predict([[footfall, tempMode, AQ, USS, CS, VOC, RP, IP, Temperature]])

    if(fail_prediction[0] == 1):
        fail_diagnosis = 'mesin rusak'
    else :
        fail_diagnosis = 'mesin tidak rusak'

    st.success(fail_diagnosis)