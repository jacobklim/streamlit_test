import streamlit as st
import pandas as pd
import os

WORK_DIR = os.path.dirname(__file__)

df = pd.read_excel(os.path.join(WORK_DIR, '../data/data.xlsx'))

st.write(df)
