# Car Sales Data Explorer
*A dynamic web application for interactive analysis and visualization of used car sales inventory data.*

### Introduction
The Car Sales Data Explorer is a Python-based web application utilizing Streamlit, designed to interactively visualize and analyze data. The application fetches data from a publicly accessible Google Sheet or, as a fallback, from a local dataset in the project directory. It leverages Plotly for interactive visualizations, and Render for cloud deployment.

### Project Overview
This project was undertaken to demonstrate proficiency in several key areas:

- Data Analysis: Exploring and analyzing car sales data to extract meaningful insights.
- Interactive Visualization: Employing Plotly to create dynamic, user-friendly visual representations of data.
- Web Development: Building and deploying a web application using Streamlit, showcasing a seamless integration of data analysis and web technologies.
- Cloud Deployment: Successfully deploying the application on Render, ensuring accessibility and scalability.

The application is ideal for users interested in the dynamics of car sales, trends in the market, or data-driven decision-making in the automotive sector.

### Dataset
The dataset, vehicles_us.csv, includes a rich collection of car sales advertisements with various attributes like make, model, year, price, and more. This dataset forms the backbone of the application, enabling a detailed exploration of trends and patterns in the used car market.

### Live Application
Experience the Car Sales Data Explorer in action: [Car Sales Data Explorer](https://used-car-market-analysis.onrender.com)

### Installation
This project uses pipenv for managing package dependencies and virtual environments. To set up this project locally:

```bash
git clone https://github.com/juansiliezar/Car-Sales-Data-Explorer.git
cd Car-Sales-Data-Explorer
pipenv install -r requirements.txt
```

### Usage
Activate the pipenv environment and run the application:

```bash
pipenv shell
streamlit run app.py
```

After execution, access the app by visiting [http://localhost:10000](http://0.0.0.0:10000) in your web browser.
