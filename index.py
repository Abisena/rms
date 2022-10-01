import streamlit as st 

st.title('Web Luas Segitiga')
st.write('Ini adalah Web menghitung luas segitiga sederhana')

alas = st.number_input('Masukan Alas', 0)
tinggi = st.number_input('Masukan tinggi', 0)
hasil = st.button('Hitung Luas')

if hasil:
    luas = 0.5 * alas * tinggi
    st.write('Luas dari segitiga itu adalah', luas)

    st.balloons()