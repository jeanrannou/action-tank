import streamlit as st

st.title('Action tank project')

@st.cahe_data
def load_data(path: str):
  data = pd.read_excel(path)
  return data

df = load_data("./Logements sociaux Paris.xlsx")
st.dataframe(df)
