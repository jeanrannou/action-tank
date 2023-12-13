import random
import pandas as pd
import streamlit as st



st.title("Bienvenue dans ce rendu")

df = pd.read_excel("LogementsSociauxParis.xlsx")
st.dataframe(df)
df["Adresse du programme"][1]*3

st.title('Partie 1 : Explorer les logements sociaux financés à Paris')
st.subheader("1.A. Combien de logements sociaux ont été financés en tout ?")
st.write('Pour répondre à cette question, nous ')

st.subheader('1.B. Combien de logements du bailleur "IMM 3F" ont été financés en 2015 ?')
filtered_df1 = df[df['Année du financement - agrément'] == 2015]
filtered_df2 = filtered_df1[filtered_df1['Bailleur social'] == 'IMM 3F']
# Calculez le nombre d'occurrences de chaque élément dans la colonne d'intérêt
occurrences = filtered_df2['Nombre total de logements financés'].value_counts()

# Affichez les résultats dans Streamlit
st.write(occurrences)

st.bar_chart(occurrences)

st.title('Titre 2')
st.write('Contenu pour le Titre 2')

st.title('Titre 3')
st.write('Contenu pour le Titre 3')

