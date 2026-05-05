import streamlit as st
import pandas as pd

df = pd.read_csv('deputados_2022.csv')
st.dataframe(df)

sigla = st.text_input('Digite a sigla de algum partido')

if sigla: 
    filtrado = df[df["partido"].str.lower() == sigla.lower()]

    if not filtrado.empty:
        st.write(f"Deputados do {sigla}:")
        st.dataframe(filtrado)
    else:
        st.write("Nenhum deputado encontrado desse partido.")
