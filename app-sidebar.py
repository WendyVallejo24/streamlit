import streamlit as st

st.title("App con Sidebar")

sidebar = st.sidebar

sidebar.title("Este es el sidebar")
sidebar.write("Datos de sidebar")

st.header("Header 1")
st.header("Header 2")
st.write("Datos del content")
