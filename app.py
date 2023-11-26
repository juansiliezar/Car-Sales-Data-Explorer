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
    df = pd.read_csv("datasets/vehicles_us.csv")    

st.title('Analyzing a Sample of the Used Car Market in the US')
st.header('Data Viewer')
st.write(df)

# -------------------------------------------------------------
# plotting the distribution of key variables with histograms
# -------------------------------------------------------------
price_hist = px.histogram(
    df, 
    x='price', 
    nbins=100, 
    title='Distribution of Vehicle Price', 
    labels={'price' : 'Vehicle Price'}
    )

model_year_hist = px.histogram(
    df, 
    x='model_year', 
    nbins=100, 
    title='Distribution of Model Years', 
    labels={'model_year' : 'Model Year'}
    )

odom_hist = px.histogram(
    df, 
    x='odometer', 
    nbins=100, 
    title='Distribution of Vehicle Mileage', 
    labels={'odometer' : 'Vehicle Mileage'}
    )

dom_hist = px.histogram(
    df, 
    x='days_listed', 
    nbins=100, 
    title='Distribution of Days on Market', 
    labels={'days_listed' : 'Days on Market'}
    )

# -------------------------------------------------------------
# Visualizng potential relationships between key variables
# -------------------------------------------------------------

price_vs_odometer = px.scatter(
    df, 
    x='odometer', y='price', 
    title='Price vs. Vehicle Mileage', 
    labels={'odometer' : 'Mileage', 
            'price' : 'Price (USD)'},
    log_x=False, log_y=False
    )

price_vs_model_year = px.scatter(
    df, 
    x='model_year', y='price', 
    title='Price vs. Model Year',
    labels={'model_year' : 'Model Year', 
            'price' : 'Price (USD)'},
    log_x=False, log_y=False
    )

st.plotly_chart(price_hist, use_container_width=True)
st.divider()

st.plotly_chart(model_year_hist, use_container_width=True)
st.divider()

st.plotly_chart(odom_hist, use_container_width=True)
st.divider()

st.plotly_chart(dom_hist, use_container_width=True)
st.divider()

log = st.checkbox('Log-Scaled Axes')
if log:
    log_x = True
    log_y = True
    
st.plotly_chart(price_vs_odometer, use_container_width=True)
st.divider()
st.plotly_chart(price_vs_model_year, use_container_width=True)