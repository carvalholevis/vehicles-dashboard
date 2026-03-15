# 🚗 Vehicles Dashboard

Interactive **web dashboard for exploring car sales advertisement data**
built with **Python, Streamlit, Pandas, and Plotly** and deployed to the
cloud using **Render**.

This project was developed as part of **Sprint 5 of the TripleTen Data
Scientist Program**. The goal of this sprint is to practice software
engineering tools and workflows that are commonly used by data
professionals.

The project focuses on:

- Creating and managing Python virtual environments
- Building an interactive web application
- Performing exploratory data analysis (EDA)
- Using Git and GitHub for version control
- Deploying a data application to the cloud

------------------------------------------------------------------------

# 🌐 Live Application

You can access the deployed dashboard here:

👉 https://vehicles-dashboard-fdn3.onrender.com/

> Note: Because the app is hosted on Render’s free tier, it may take a
> few seconds to wake up if it has been inactive.

------------------------------------------------------------------------

# 📂 Project Repository

GitHub repository:

👉 https://github.com/carvalholevis/vehicles-dashboard

------------------------------------------------------------------------

# 📊 Project Overview

This application provides an **interactive dashboard** that allows users
to explore data from a dataset of **car sale advertisements in the
United States**.

The dashboard includes:

- Dataset viewer
- Manufacturer filtering
- Interactive visualizations
- Histogram analysis
- Price comparison between manufacturers

All visualizations are built using **Plotly Express**, allowing users to
interact with charts directly in the browser.

------------------------------------------------------------------------

# ⚙️ Technologies Used

The following technologies were used in this project:

- **Python**
- **Streamlit** — Web application framework
- **Pandas** — Data manipulation and analysis
- **Plotly Express** — Interactive data visualization
- **Git & GitHub** — Version control
- **Render** — Cloud deployment platform
- **Jupyter Notebook** — Exploratory Data Analysis

------------------------------------------------------------------------

# 📁 Project Structure

    .
    ├── README.md
    ├── app.py
    ├── vehicles_us.csv
    ├── requirements.txt
    ├── notebooks
    │   └── EDA.ipynb
    └── .streamlit
        └── config.toml

### File Description

**app.py**  
Main Streamlit application responsible for generating the dashboard.

**vehicles_us.csv**  
Dataset containing car advertisement data.

**requirements.txt**  
Lists the Python dependencies required to run the application.

**notebooks/EDA.ipynb**  
Jupyter Notebook used for the initial exploratory data analysis.

**.streamlit/config.toml**  
Configuration file required to run Streamlit correctly on Render.

------------------------------------------------------------------------

# 📈 Dashboard Features

## 1️⃣ Data Viewer

Users can view the dataset directly in the dashboard.

A checkbox allows filtering manufacturers with fewer than **1000
advertisements**.

Features:

- Interactive data table
- Manufacturer filtering

------------------------------------------------------------------------

## 2️⃣ Vehicle Types by Manufacturer

A **stacked bar chart** shows how different vehicle types are
distributed across manufacturers.

This visualization helps identify:

- Manufacturer specialization
- Popular vehicle categories
- Distribution of vehicle types

------------------------------------------------------------------------

## 3️⃣ Vehicle Condition vs Model Year

A **histogram visualization** showing how vehicle condition relates to
model year.

This chart helps explore:

- Condition distribution
- Age of vehicles listed
- Trends across model years

------------------------------------------------------------------------

## 4️⃣ Price Distribution Comparison

Users can compare **price distributions between two manufacturers**.

Features:

- Select two manufacturers
- Overlay histogram comparison
- Optional normalization

This helps analyze:

- Price ranges
- Market positioning
- Differences between manufacturers

------------------------------------------------------------------------

# 🧹 Data Cleaning

Basic preprocessing steps applied before visualization:

- Missing values in `is_4wd` and `cylinders` filled with 0
- Missing `paint_color` filled with `"unknown"`
- Missing `odometer` replaced with the median value
- Rows missing `model_year`, `model`, or `condition` removed
- Manufacturer extracted from the `model` column

These steps help ensure cleaner and more reliable visualizations.

------------------------------------------------------------------------

# 🚀 Running the Project Locally

Clone the repository:

    git clone https://github.com/carvalholevis/vehicles-dashboard.git

Navigate to the project directory:

    cd vehicles-dashboard

Install dependencies:

    pip install -r requirements.txt

Run the Streamlit app:

    streamlit run app.py

------------------------------------------------------------------------

# ☁️ Deployment

This project is deployed using **Render**.

Deployment configuration:

**Build Command**

    pip install --upgrade pip && pip install -r requirements.txt

**Start Command**

    streamlit run app.py

------------------------------------------------------------------------

# 👨‍💻 Author

**Leviton Lima Carvalho**

📧 Email: levitoncarvalho@icloud.com  
💻 GitHub: https://github.com/carvalholevis

------------------------------------------------------------------------

# 📌 Project Context

This project was created as part of **Sprint 5 of the TripleTen Data
Scientist Program**, which focuses on practicing real-world software
engineering tools used by data professionals.

The sprint emphasizes:

- Building a web application with **Streamlit**
- Working with **GitHub repositories**
- Creating **virtual environments**
- Deploying applications to the **cloud**
- Developing **interactive dashboards for data exploration**

------------------------------------------------------------------------

⭐ Feel free to explore the repository and try the live dashboard!
