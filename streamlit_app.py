import streamlit as st
pip install st-gsheets-connection

st.title('Actionnn')

# URL du fichier Excel sur GitHub
url = 'https://github.com/jeanrannou/action-tank/blob/main/Logements%20sociaux%20Paris.xlsx?raw=true'

# Lire le fichier Excel
df = pd.read_csv(url)

# Afficher le DataFrame
st.write(df)
