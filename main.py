import streamlit as st
import pandas as pd
import numpy as np
from io import StringIO
import requests

# Show title of the app
st.title('POAP Link Checker')

uploaded_file = st.file_uploader("Upload your .txt file containing your POAP links")

if uploaded_file:
    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))

    # To read file as string:
    lines = stringio.readlines()
    lines = [line.strip() for line in lines]

    st.write("File uploaded! You have", len(lines), "POAPs. Continue further or remove the file by pressing the X key.")

st.divider()

if uploaded_file:
    st.button("Check my POAPs' validity!")