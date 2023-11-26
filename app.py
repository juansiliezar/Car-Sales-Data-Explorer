import pandas as pd 
import streamlit as st 
import plotly.express as px
import requests
from io import BytesIO

# 
# trying to read in dataset from google sheet i made public 
# and then loading it from the project directory if it fails
# 
try:  
    sheet_url = "https://docs.google.com/spreadsheets/d/1jzihXIadik_fkLF3u5dtNW2ELG0Ts3CNjOMFAVnrPL0/edit?usp=sharing"
    r = requests.get(sheet_url)   
    df = pd.read_csv(BytesIO(r.content)) 
    
except:   
    df = pd.read_csv("datasets/vehicles_us.csv")    

# 
# Adding a title to the page
# 
st.title('Car Sales Data Explorer')

#
# and displaying the dataset with a header labeling it
# 
st.header('Dataset')
st.write(df)

# 
# Visualizing Distribution of Vehicle Price with a Histogram
# 
price_hist = px.histogram(
    df, 
    x='price', 
    nbins=100, 
    title='Distribution of Vehicle Price', 
    labels={'price' : 'Vehicle Price'}
    )

# 
# Displaying Plot
# 
st.plotly_chart(price_hist, use_container_width=True)
st.divider()

# 
# Visualizing Distribution of Model Year with a Histogram
# 
model_year_hist = px.histogram(
    df, 
    x='model_year', 
    nbins=100, 
    title='Distribution of Model Years', 
    labels={'model_year' : 'Model Year'}
    )

# 
# Displaying Plot
# 
st.plotly_chart(model_year_hist, use_container_width=True)
st.divider()

# 
# Visualizing Distribution of Vehicle Mileage with a Histogram
# 
odom_hist = px.histogram(
    df, 
    x='odometer', 
    nbins=100, 
    title='Distribution of Vehicle Mileage', 
    labels={'odometer' : 'Vehicle Mileage'}
    )

# 
# Displaying Plot
# 
st.plotly_chart(odom_hist, use_container_width=True)
st.divider()

# 
# Visualizing Distribution of Days on Market with a Histogram
#
dom_hist = px.histogram(
    df, 
    x='days_listed', 
    nbins=100, 
    title='Distribution of Days on Market', 
    labels={'days_listed' : 'Days on Market'}
    )
#
# Displaying Plot
# 
st.plotly_chart(dom_hist, use_container_width=True)
st.divider()

#
# Adding a checkbox option to view graph's axes scaled logarithmically
# and adjusting the corresponding parameters depending on input
#
log = st.checkbox('View Log-Scaled Axes on Price vs. Mileage')
if log:
    log_x = True
    log_y = True
else:
    log_x = False
    log_y = False
# 
# Creating Price vs. Odometer Scatter Plot
#
price_vs_odometer = px.scatter(
    df, 
    x='odometer', y='price', 
    title='Price vs. Vehicle Mileage', 
    labels={'odometer' : 'Mileage', 
            'price' : 'Price (USD)'},
    log_x=log_x, log_y=log_y
    )

#
# Displaying Plot
#    
st.plotly_chart(price_vs_odometer, use_container_width=True)
st.divider()
 
# 
# Adding a checkbox option to view graph's axes scaled logarithmically
# and adjusting the corresponding parameters depending on input
# 
log_2 = st.checkbox('View Log-Scaled Axes on Price vs. Model Year')
if log_2:
    log_x = True
    log_y = True
else:
    log_x = False
    log_y = False
    
# 
# Creating Price vs. Model Year Scatter Plot
#   
price_vs_model_year = px.scatter(
    df, 
    x='model_year', y='price', 
    title='Price vs. Model Year',
    labels={'model_year' : 'Model Year', 
            'price' : 'Price (USD)'},
    log_x=False, log_y=False
    )

# 
# Displaying Plot
# 
st.plotly_chart(price_vs_model_year, use_container_width=True)



    
