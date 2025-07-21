import streamlit as st
import pandas as pd
import plotly.express as px

# Load your CSV file
df = pd.read_csv(r'PSales.csv')

# Title
st.title("Product Sales Dashboard")

# Category selection
categories = df['Category'].unique()
selected_categories = st.multiselect(
    "Select Category:",
    options=categories,
    default=None
)

# Filter DataFrame based on selection
if selected_categories:
    filtered_df = df[df['Category'].isin(selected_categories)]

    # Bar Chart
    bar_data = filtered_df.groupby('SubCategory')['Sales'].sum().reset_index()
    bar_fig = px.bar(
        bar_data,
        x='SubCategory',
        y='Sales',
        title='Sales by SubCategory',
        labels={'Sales': 'Total Sales'}
    )
    st.plotly_chart(bar_fig, use_container_width=True)

    # Pie Chart
    pie_data = filtered_df.groupby('SubCategory')['Profit'].sum().reset_index()
    pie_fig = px.pie(
        pie_data,
        names='SubCategory',
        values='Profit',
        title='Profit by SubCategory'
    )
    st.plotly_chart(pie_fig, use_container_width=True)

    # Sunburst Chart
    sunburst_fig = px.sunburst(
        filtered_df,
        path=['Category', 'SubCategory', 'Discount'],
        values='Discount',
        title='Discount Breakdown'
    )
    st.plotly_chart(sunburst_fig, use_container_width=True)
else:
    st.info("Please select at least one category to see the charts.")