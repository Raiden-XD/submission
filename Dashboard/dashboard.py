# -*- coding: utf-8 -*-
"""dashboard.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1vWGW1EOdsYRLfY1GQpZzxqLdQh4nYcNH
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Judul Dashboard
st.title("Dashboard Penyewaan Sepeda")

# Memuat data
@st.cache_data  # Perbarui dekorator caching
def load_data():
    data = pd.read_csv('Dashboard/day.csv')  # Ganti dengan path yang sesuai jika perlu
    return data

# Memanggil fungsi untuk memuat data
data = load_data()

# Menampilkan data
st.subheader("Data Penyewaan Sepeda")
st.write(data.head())  # Tampilkan 5 baris pertama

# Statistik Deskriptif
st.subheader("Statistik Deskriptif")
st.write(data.describe())

# Visualisasi Jumlah Penyewaan per Musim
st.subheader("Jumlah Penyewaan Sepeda per Musim")
season_count = data.groupby('season')['cnt'].sum()
st.bar_chart(season_count)

# Visualisasi Penyewaan per Hari dalam Minggu
st.subheader("Jumlah Penyewaan Sepeda per Hari dalam Minggu")
weekday_count = data.groupby('weekday')['cnt'].sum()
st.bar_chart(weekday_count)

# Input dari Pengguna
st.sidebar.header("Pengaturan")
season_filter = st.sidebar.selectbox("Pilih Musim:", options=data['season'].unique())
filtered_data = data[data['season'] == season_filter]

# Visualisasi Penyewaan untuk Musim Terpilih
st.subheader(f"Penyewaan Sepeda pada Musim {season_filter}")
st.line_chart(filtered_data['cnt'])

# Kesimpulan
st.subheader("Kesimpulan")

st.markdown("""
**1. Pengaruh Musim terhadap Penyewaan Sepeda:**
   Berdasarkan visualisasi, musim memiliki pengaruh yang signifikan terhadap jumlah penyewaan sepeda. Misalnya, musim panas mungkin menunjukkan jumlah penyewaan yang lebih tinggi dibandingkan dengan musim dingin.

**2. Tren Penyewaan Berdasarkan Hari dalam Seminggu:**
   Jumlah penyewaan sepeda bervariasi sepanjang minggu, di mana akhir pekan cenderung menunjukkan peningkatan penyewaan. Ini dapat diartikan bahwa orang lebih banyak menggunakan sepeda untuk rekreasi pada hari libur.

**3. Pola Penyewaan dalam Kondisi Cuaca:**
   Kondisi cuaca juga berpengaruh terhadap jumlah penyewaan sepeda. Hari-hari dengan cuaca yang lebih baik cenderung menarik lebih banyak pengguna untuk menyewa sepeda dibandingkan dengan hari berawan atau hujan.

**4. Implikasi untuk Manajemen Penyewaan:**
   Informasi ini berguna bagi manajemen untuk menyiapkan lebih banyak sepeda di musim panas atau akhir pekan ketika permintaan lebih tinggi, dan mengurangi penyediaan sepeda di hari kerja atau musim dingin.
""")
