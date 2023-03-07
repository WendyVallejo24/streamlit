import pandas as pd
import streamlit as st
import codecs
import numpy as np

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
agree = st.sidebar.checkbox("Show row data ")
if agree:
  st.dataframe(data)

if st.sidebar.checkbox('Recorridos por hora'):
    st.subheader('Histograma de Numero de recorridos por hora')

    hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
    st.bar_chart(hist_values)
