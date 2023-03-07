import pandas as pd
import streamlit as st
import codecs

DATA_URL = 'citibike-tripdata.csv'

@st.cache
def load_data(nrows):
    DATA_URL = codecs.open('citibike-tripdata.csv','rU','latin1')
    data = pd.read_csv(DATA_URL, nrows=nrows)
    return data

data_load_state = st.text('Cargando...')
data = load_data(500)
data_load_state.text('Done! (using st.cache)')
st.dataframe(data)