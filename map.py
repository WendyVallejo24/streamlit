import streamlit as st
import numpy as np
import pandas as pd

map_data = pd.DataFrame(
    np.random.randn(10, 2) / [500, 500] + [18.853354, -97.068924],
    columns=['lat', 'lon']
)

st.map(map_data)