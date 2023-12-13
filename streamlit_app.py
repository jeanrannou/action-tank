import random
import pandas as pd
import streamlit as st



st.title("Bienvenue dans ce rendu")

df = pd.read_excel("LogementsSociauxParis.xlsx")
st.dataframe(df)
df["Adresse du programme"][1]*3

st.sidebar.title("Menu de Défilement")
if st.sidebar.button("Accueil"):
    st.markdown("<a href='#accueil'>Accueil</a>", unsafe_allow_html=True)
if st.sidebar.button("Section 1"):
    st.markdown("<a href='#section1'>Section 1</a>", unsafe_allow_html=True)
if st.sidebar.button("Section 2"):
    st.markdown("<a href='#section2'>Section 2</a>", unsafe_allow_html=True)
if st.sidebar.button("Section 3"):
    st.markdown("<a href='#section3'>Section 3</a>", unsafe_allow_html=True)

# Contenu de la page avec des ancres HTML
st.markdown("## Accueil")
st.write("C'est la première section de votre application.")
st.markdown("<a name='accueil'></a>", unsafe_allow_html=True)

st.markdown("## Section 1")
st.write("Contenu de la première section.")
st.markdown("<a name='section1'></a>", unsafe_allow_html=True)

st.markdown("## Section 2")
st.write("Contenu de la deuxième section.")
st.markdown("<a name='section2'></a>", unsafe_allow_html=True)

st.markdown("## Section 3")
st.write("Contenu de la troisième section.")
st.markdown("<a name='section3'></a>", unsafe_allow_html=True)
