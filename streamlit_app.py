import random
import pandas as pd
import streamlit as st



st.title("Bienvenue dans ce rendu")

df = pd.read_excel("LogementsSociauxParis.xlsx")
st.dataframe(df)
df["Adresse du programme"][1]*3

# Options du menu latéral
menu_options = ["Accueil", "Section 1", "Section 2"]

# Sélection de l'option du menu latéral
selected_option = st.sidebar.radio("Menu", menu_options)

# Contenu en fonction de l'option sélectionnée
if selected_option == "Accueil":
    st.header("Bienvenue sur la page d'accueil")
    st.write("C'est la première section de votre application.")
elif selected_option == "Section 1":
    st.header("Section 1")
    st.write("Contenu de la première section.")
elif selected_option == "Section 2":
    st.header("Section 2")
    st.write("Contenu de la deuxième section.")
