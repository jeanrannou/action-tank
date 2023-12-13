import streamlit as st

st.title('Action tank')

# URL du fichier Excel sur GitHub
url = 'https://github.com/jeanrannou/action-tank/blob/main/Logements%20sociaux%20Paris.xlsx?raw=true'

# Lire le fichier Excel
df = pd.read_excel(url)

# Afficher le DataFrame
st.write(df)
