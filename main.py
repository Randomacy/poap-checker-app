# import libraries
import streamlit as st
import pandas as pd
import numpy as np
from io import StringIO
import requests
from datetime import date

# Declare variables
headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36'}
api_endpoint = "https://frontend.poap.tech/actions/claim-qr?qr_hash="
link_list = []
validity_list = []

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
        progress_text = "Operation in progress. Please wait."        
        st.write("Checking POAPs now")
        for line_num in range(len(lines)):
            if 'app' in lines[line_num]:
                temp_hash = lines[line_num].replace("https://app.poap.xyz/claim/", "")
            else:
                temp_hash = lines[line_num].replace("http://POAP.xyz/claim/", "")
            
            temp_endpoint = api_endpoint + temp_hash
            temp_res = requests.get(temp_endpoint,
                                    headers = headers)
            temp_json = temp_res.json()
            
            try:
                if temp_json['claimed']:
                    st.write(lines[line_num], "is claimed")
                    validity_list.append('CLAIMED')
                else:
                    st.write(lines[line_num], "is still ok")
                    validity_list.append('NOT CLAIMED')
            except:
                validity_list.append('ERROR')

        df = pd.DataFrame({"POAP_URL": lines, 
                           "Claimed?": validity_list})

        csv = df.to_csv(index = None).encode('utf-8')
        
        st.download_button(
                        label="Download data as CSV",
                        data=csv,
                        file_name='checked_poap_links.csv',
                        mime='text/csv',
                        )

    else:
        print(date.today(), "Validity Check Ready")


