import streamlit as st
import pandas as pd

st.title("Streamlit - Search ranges")
DATA_URL = "https://firebasestorage.googleapis.com/v0/b/streamlit-wv.appspot.com/o/csv%2Fwbpat%2Fdataset.csv?alt=media&token=5d24c3bb-e44c-4779-8b4d-06b48023d1d0"

@st.cache
def load_data_byrange(startid, endid):
    data = pd.read_csv(DATA_URL)
    filtered_data_byrange = data[ (data["index"] >= startid) & (data["index"] <= endid) ]
    return filtered_data_byrange

startid = st.text_input("Start index: ")
endid = st.text_input("End index: ")
btnRange = st.button("Search by range ")

if (btnRange):
    filterbyrange = load_data_byrange(int(startid), int(endid))
    count_row = filterbyrange.shape[0]
    st.write(f"Total items: {count_row}")

    st.dataframe(filterbyrange)
