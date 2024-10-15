import streamlit as st
import pandas as pd
import math
from pathlib import Path


df = pd.read_excel('logbook.xlsx')

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

''

st.table(df)
