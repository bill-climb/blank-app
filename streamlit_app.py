import streamlit as st
import pandas as pd
import math
from pathlib import Path

@st.cache_data
def get_ukc_data():
    """Grab ukc data from a xlsx file.

    This uses caching to avoid having to read the file every time. If we were
    reading from an HTTP endpoint instead of a file, it's a good idea to set
    a maximum age to the cache with the TTL argument: @st.cache_data(ttl='1d')
    """

    # Instead of a CSV on disk, you could read from an HTTP endpoint here too.
    DATA_FILENAME = Path(__file__).parent/'data/logbook.xlsx'
    df = pd.read_excel(DATA_FILENAME)
    df[['style','style category']] = df['Style'].str.split(' ',expand=True)
    df=df.drop(columns=['Style'])
    df.rename(columns={'Partner(s)': 'Partner'}, inplace=True)
    #add index
    df['log_id'] = df.index + 1
    #convert date
    df['Date']=pd.to_datetime(df['Date'], format='%d/%b/%y')
    #only show rows from this year
    df=df[(df['Date'] > start_date)]
    df["first star"]= df["Grade"].str.find('*')
    df[['overall grade','technical grade', 'star rating']] = df['Grade'].str.split(' ',expand=True)

    return df

ukc_df = get_ukc_data()



st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

''

st.table(ukc_df)
