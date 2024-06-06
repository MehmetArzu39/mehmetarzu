import streamlit as st 
import pandas as pd



import streamlit as st
import pandas as pd

# GitHub'daki Excel dosyasının URL'si
url = "https://raw.githubusercontent.com/MehmetArzu39/mehmetarzu/main/6%20class%20csv.csv"

# Excel dosyasını yükleyip okuma
@st.cache
def load_data(url):
    return pd.read_csv(url)

# Veriyi yükle
df = load_data(url)

# Streamlit ile veriyi görüntüleme
st.write("Dosya Başarıyla Yüklendi!")
st.write("Dosya İçeriği:")
st.write(df)



