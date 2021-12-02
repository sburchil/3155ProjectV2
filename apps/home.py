import streamlit as st
import pandas as pd
import numpy as np
from data.create_data import create_table
import plotly.graph_objects as go

def app():

    st.title('Home')

    st.write("This is a sample home page in the mutliapp.")
    st.write("See `apps/home.py` to know how to use it.")

    st.write('Navigate to `Data Stats` page to visualize the data')
    choice = ''
    df = create_table(choice)
    st.write(df)