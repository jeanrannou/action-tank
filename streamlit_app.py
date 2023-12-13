import random
import pandas as pd
import streamlit as st



st.title("Bienvenue dans ce rendu")

df = pd.read_excel("LogementsSociauxParis.xlsx")
st.dataframe(df)
df["Adresse du programme"][1]*3

st.title('Titre 1')
st.write('Contenu pour le Titre 1')

st.title('Titre 2')
st.write('Contenu pour le Titre 2')

st.title('Titre 3')
st.write('Contenu pour le Titre 3')
