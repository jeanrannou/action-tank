import streamlit as st

st.title('Action tank project')

@st.cache_data
def load_data(path: str):
  data = pd.read_excel(path)
  return data

df = load_data("https://github.com/jeanrannou/action-tank/blob/794a072e1079e6fb09cd5e4fde7949f79a59cc38/Logements%20sociaux%20Paris.xlsx?raw=true")
st.dataframe(df)
