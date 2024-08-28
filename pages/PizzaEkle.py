import streamlit as st
import sqlite3

conn = sqlite3.connect("pizzadb.sqlite3")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS pizzalar(isim TEXT,smFiyat REAL,mdFiyat REAL,lgFiyat REAL,icindekiler "
               "TEXT,resim TEXT)")
conn.commit()
st.header("Pizza Ekle")

with st.form("pizzaEkle", clear_on_submit=True):
    isim = st.text_input("Pizza İsmi")
    smFiyat = st.number_input("Small Fiyat")
    mdFiyat = st.number_input("Medium Fiyat")
    lgFiyat = st.number_input("Large Fiyat")
    icindekiler = st.multiselect("İçindekiler", ["Mantar", "biber", "domates", "fesleğen",
                                                 "sucuk", "sosis", "jambon", "tavuk", "pastırma"])

    resim = st.file_uploader("Pizza resmi ekleyiniz")

    submit_button = st.form_submit_button("Pizza Ekle")

    if submit_button:

        icindekiler=str(icindekiler)
        icindekiler=icindekiler.replace("[","")
        icindekiler=icindekiler.replace("]","")
        icindekiler=icindekiler.replace("'","")

        resimurl="images/"+resim.name
        st.write(resimurl)

        open(resimurl,"wb").write(resim.read())

        cursor.execute("INSERT INTO pizzalar VALUES(?,?,?,?,?,?)",(isim,smFiyat,mdFiyat,lgFiyat,icindekiler,resimurl))
        conn.commit()



