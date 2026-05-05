import streamlit as st
import pandas as pd

df = pd.read_csv('deputados_2022.csv')


sigla = st.text_input('Digite a sigla de algum partido')

if sigla: 
    filtrado = df[df["partido"].str.lower() == sigla.lower()]

    if not filtrado.empty:
        st.write(f"Deputados do {sigla}:")
        st.dataframe(filtrado)
    else:
        st.write("Nenhum deputado encontrado desse partido.")
 

if "sexo" in filtrado.columns:
            filtrado = filtrado.copy()
            filtrado["sexo"] = filtrado["sexo"].str.upper()

            contagem = filtrado["sexo"].value_counts()

          
            contagem.index = contagem.index.map({"M": "Homens","F": "Mulheres"})

            st.write("Distribuição por gênero:")
            st.bar_chart(contagem)
    else:
            st.write("Coluna 'sexo' não encontrada no dataset.")

    else:
        st.write("Nenhum deputado encontrado desse partido.")
