import pandas as pd
import streamlit as st
import codecs

DATA_URL = 'citibike-tripdata.csv'
DATE_COLUMN = 'started_at'

st.title('Cicle Ride in New York')
st.sidebar.image('credencial.jpg')
st.sidebar.write('zS20006733@estudiantes.uv.mx')
st.sidebar.write("Wendy Belén Vallejo Patraca")
st.sidebar.write("S20006733")

@st.cache
def load_data(nrows):
    DATA_URL = codecs.open('citibike-tripdata.csv','rU','latin1')
    data = pd.read_csv(DATA_URL, nrows=nrows)
    return data

data_load_state = st.text('Cargando...')
data = load_data(500)
data_load_state.text('Done! (using st.cache)')

st.header("Dataset")
agree = st.sidebar.checkbox("show DataSet Overview ? ")
if agree:
  st.dataframe(data)