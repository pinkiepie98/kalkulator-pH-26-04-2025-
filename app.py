import streamlit as st
import math

st.markdown("""
    <style>
    .main {
        background-color: #99BC85;
        padding: 20px;
        border-radius: 10px;
    }
    .title {
        color: #E4EFE7;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main">', unsafe_allow_html=True)
st.markdown('<h1 class="title">🧫 Kalkulator Koloni Bakteri 🦠 </h1>', unsafe_allow_html=True)



st.write("Aplikasi sederhana untuk menghitung jumlah koloni bakteri per mL sampel berdasarkan jumlah koloni, faktor pengenceran, dan volume inokulasi.")

Input user
jumlah_koloni = st.number_input("Masukkan jumlah koloni:", min_value=0, step=1)
faktor_pengenceran = st.number_input("Masukkan faktor pengenceran:", min_value=1, step=1)
volume_inokulasi = st.number_input("Masukkan volume inokulasi (dalam mL):", min_value=0.01, step=0.01)

Tombol Hitung
if st.button("Hitung Koloni"):
    if volume_inokulasi > 0:
        hasil = jumlah_koloni / (faktor_pengenceran * volume_inokulasi)
        st.success(f"Hasil perhitungan: {hasil:.2f} CFU/mL")
    else:st.error("Volume inokulasi tidak boleh nol!")

st.markdown('</div>', unsafe_allow_html=True)

