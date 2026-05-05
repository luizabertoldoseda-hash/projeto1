import streamlit as st

st.title('Luiza S')
st.write("Esse é o meu texto")

nome = st.text_input('Digite o seu nome')
if nome:
    st.write(nome,'loves tung tung tung sahur!')
  
st.image("https://images.cults3d.com/Cysw2zADhd70OdIduOOQtXqfSyA=/516x516/filters:no_upscale():format(webp)/https://fbi.cults3d.com/uploaders/38920753/illustration-file/626491b5-8223-499a-869a-08b114c95cfb/tung-tung.jpg", caption="Legenda da Imagem", use_container_width=True)
st.video("https://www.youtube.com/watch?v=LXUSaVw3Mvk")
