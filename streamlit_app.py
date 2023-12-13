import random
import pandas as pd
import streamlit as st
from st_aggrid import AgGrid



st.title("Coucou")

df = pd.read_excel("LogementsSociauxParis.xlsx")
AgGrid(df)
