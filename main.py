import streamlit as st
import pandas as pd
import numpy as np
from io import StringIO
import requests

# Declare variables

# Show title of the app
st.title('POAP Link Checker')

uploaded_file = st.file_uploader("Upload your .txt file containing your POAP links")

if uploaded_file:
    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))

    # To read file as string:
    lines = stringio.readlines()
    lines = [line.strip() for line in lines]

    st.write("File uploaded! You have", len(lines), "POAPs")
    st.write("Continue further or remove the file by pressing the X key.")

if uploaded_file:
    if st.button("Check my POAPs' validity!"):
        print("Hello")
    else:
        print("Validity Check Ready")
