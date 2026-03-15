import streamlit as st
import pandas as pd 
import plotly.express as px

car_data = pd.read_csv("vehicles.csv") #READING CSV DATA

st.title('Car Sales Ads Dashboard') #Dashboard Title

#DATA CLEANING

car_data['is_4wd'] = car_data['is_4wd'].fillna(0)
car_data['cylinders'] = car_data['cylinders'].fillna(0)
car_data['paint_color'] = car_data['paint_color'].fillna('unknown')
car_data['odometer'] = car_data['odometer'].fillna(car_data['odometer'].median())
car_data = car_data.dropna(subset=['model_year', 'model', 'condition'])

#will be needed to extract the manufacturer from the Model column
car_data['manufacturer'] = car_data['model'].str.split().str[0]

#FIRST PART
st.header('Data viewer') #Data viewer title
include_less_ads = st.checkbox('Include manufacturers with less than 1000 ads')

#Function to make the checkbox work
if include_less_ads:
    count_ads = car_data['manufacturer'].value_counts()
    small_manufacturers = count_ads[count_ads < 1000].index
    car_data_filtered = car_data[car_data['manufacturer'].isin(small_manufacturers)]
else:
    car_data_filtered = car_data

#Showing the table
st.dataframe(car_data_filtered)



#SECOND PART
st.header('Vehicles types by manufacturer')


# Count the quantity of each type by manufacturer
type_count = car_data.groupby(['manufacturer', 'type']).size().reset_index(name='count')

# Creating the bar chart
fig_types = px.bar(
    type_count,
    x='manufacturer',
    y='count',
    color='type',
    title='Quantity of each type by manufacturer',
    barmode='stack'
)
st.plotly_chart(fig_types, use_container_width=True)

#THIRD PART
st.header('Histogram of condition vs model_year')

#available conditions
car_data['condition'] = car_data['condition'].astype(str)

#Creating the histogram
fig_condition = px.histogram(
    car_data,
    x='model_year',
    color='condition',
    title='Histogram of condition vs model_year',
    barmode='stack'
)
st.plotly_chart(fig_condition, use_container_width=True)

#FOURTH PART
st.header('Compare price distribution between manufacturers')

# List of unique manufacturers (sorted)
manufacturers = sorted(car_data['manufacturer'].unique())

# Selectors for the manufacturers
manufacturer_1 = st.selectbox('Select manufacturer 1', manufacturers, index=0)
manufacturer_2 = st.selectbox('Select manufacturer 2', manufacturers, index=1 if len(manufacturers) > 1 else 0)

# Box for normalization
normalize = st.checkbox('Normalize histogram')

#Filtering the data     
car_data_comp = car_data[car_data['manufacturer'].isin([manufacturer_1, manufacturer_2])]

fig_comp = px.histogram(
    car_data_comp,
    x='price',
    color='manufacturer',
    title=f'Compare price distribution between {manufacturer_1} vs {manufacturer_2}',
    barmode='overlay',
    histnorm='percent' if normalize else None,
    color_discrete_sequence=['red', 'green'],
    nbins=40
)
st.plotly_chart(fig_comp, use_container_width=True)

