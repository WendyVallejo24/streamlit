import pandas as pd
import streamlit as st
import numpy as np

sidebar = st.sidebar
DATA_URL = 'citibike-tripdata.csv'
DATE_COLUMN = 'started_at'

st.title('Cicle Ride in New York')
st.sidebar.image('credencial.jpg')
st.sidebar.write('Correo Electronico')
st.sidebar.write('zS20006733@estudiantes.uv.mx')
st.sidebar.write("Wendy Belén Vallejo Patraca")
st.sidebar.write("S20006733")

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    data.rename({'start_lat': 'lat', 'start_lng': 'lon'}, axis=1, inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])

    return data

data_load_state = st.text('Cargando...')
data = load_data(500)
data_load_state.text('Done! (using st.cache)')

if st.sidebar.checkbox("Show row data "):
  st.subheader('Raw Data')
  st.write(data)

if st.sidebar.checkbox('Recorridos por hora'):
    st.subheader('Histograma de Numero de recorridos por hora')

    hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
    st.bar_chart(hist_values)

hour_to_filter = sidebar.slider('hour', 0, 23, 15)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

st.subheader('Map of all pickups at %s:00' % hour_to_filter)
st.map(filtered_data)