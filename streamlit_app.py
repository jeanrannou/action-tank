import random
import pandas as pd
import streamlit as st



st.title("Yooo")

df = pd.read_excel("LogementsSociauxParis.xlsx")
st.dataframe(df)
df["Adresse du programme"][1]*3
