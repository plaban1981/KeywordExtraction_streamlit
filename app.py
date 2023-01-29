import streamlit as st
from PIL import Image
import requests
import pandas as pd
import os
import json
#
image_path = "image.png"
image = Image.open(image_path)

st.set_page_config(page_title="Keywords Extraction App", layout="centered")
st.image(image, caption='Keywords Extraction')
#
# page header
st.title(f"Keywords Extraction App")
with st.form("Generate"):
   text1 = st.text_input("Enter text here")
   submit = st.form_submit_button("Extract Keywords")
   #
   if submit:    
        print(text1)
        #
        with open("input.txt", "wb") as f:
            f.write(text1.encode("utf-8"))
        os.chmod("input.txt", 0o777)
        # Paraphrase Generation API
        url = "https://app.aimarketplace.co/api/marketplace/models/detect-keyword-from-the-text-68658c4a/predict/"
        payload={'data': open('input.txt','rb')}
        headers = {'Authorization': 'Api-Key abcPr3wM.PYlSv8825pddVSvjuZ3BAa0Ri9CXguIg'}

        response = requests.request("POST", url, headers=headers, files=payload)

        #print(type(response))
        #print(response.json()['output'])
        #print(response.text)
        #print(response.text.split("Predictions: [")[1].split("]")[0])
        print(response.text)
        # output header
        st.header("Keywords Extracted")
        # output results
        st.success(response.text.split("detected ")[1].split("}")[0])