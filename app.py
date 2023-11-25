import pandas as pd 
import streamlit as st 
import plotly.express as px
import requests
from io import BytesIO

# -------------------------------------------------------------
# trying to read in dataset from google sheet i made public 
# and then loading it from the project directory if it fails
# -------------------------------------------------------------
try:  
    sheet_url = "https://docs.google.com/spreadsheets/d/1jzihXIadik_fkLF3u5dtNW2ELG0Ts3CNjOMFAVnrPL0/edit?usp=sharing"
    r = requests.get(sheet_url)   
    df = pd.read_csv(BytesIO(r.content)) 
    
except:   
    df = pd.read_csv("/Users/juansiliezar/sprint-4-software-development-tools/datasets/vehicles_us.csv")
    

st.write('Data Viewer')
st.write(df)