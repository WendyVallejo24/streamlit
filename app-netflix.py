import pandas as pd
import streamlit as st
import codecs

DATA_URL = codecs.open('movies.csv', 'rU', 'latin1')

st.title('Netflix app')
st.sidebar.image('logo.jpg')
st.sidebar.write("Wendy Belén Vallejo Patraca")
st.sidebar.write("S20006733")

@st.cache
def load_data(nrows):
    DATA_URL = codecs.open('movies.csv','rU','latin1')
    data = pd.read_csv(DATA_URL, nrows=nrows)
    return data

data_load_state = st.text('Cargando...')
data = load_data(500)
data_load_state.text('Done! (using st.cache)')

st.dataframe(data)

sidebar=st.sidebar
agree=sidebar.checkbox("Deseas ver los films recuperados?")
if agree:
    load_data(500)

@st.cache
def load_data_byname(name):
    data =pd.read_csv(DATA_URL)
    filtered_data_byname =data[data["name"].str.contains(name)]
    return filtered_data_byname

name = sidebar.text_input("Titulo del filme")
btnbuscar = sidebar.button('Buscar filme')

if(btnbuscar):
    filterbyname = load_data_byname(name)
    count_row = filterbyname.shape[0]
    st.write("total names: {count_row}")

    st.dataframe(filterbyname)

#selected box
@st.cache
def load_data_bydir(direct):
    data =pd.read_csv(DATA_URL)
    filtered_data_bydir = data[data['director'] == direct]

    return filtered_data_bydir

selected_sex =sidebar.selectbox('Seleccionar director ', data['director'].unique())
btndirector = sidebar.button('filtrar')

if(btndirector):
    filterbysex =load_data_bydir(selected_sex)
    count_row = filterbysex.shape[0]
    st.write(f"Total items: {count_row}")

    st.dataframe(filterbysex)