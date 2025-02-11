import streamlit as st
import pandas as pd
from data_generator import generate_mock_data, get_category_banners
from utils import (create_sales_by_category_chart, create_sales_trend_chart,
                   create_top_products_chart, create_geographic_sales_chart,
                   calculate_key_metrics)

# Page configuration
st.set_page_config(
    page_title="E-commerce Analytics Dashboard",
    page_icon="🛍️",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .css-1d391kg {
        padding-top: 1rem;
    }
    .stMetric {
        background-color: #f0f2f6;
        padding: 15px;
        border-radius: 5px;
    }
    .category-banner {
        width: 100%;
        height: 200px;
        object-fit: cover;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Load data
@st.cache_data
def load_data():
    return generate_mock_data()

df = load_data()
category_banners = get_category_banners()

# Sidebar filters
st.sidebar.title("Filters")

# Date filter
min_date = df['date'].min().date()
max_date = df['date'].max().date()

start_date = st.sidebar.date_input(
    "Start Date",
    value=min_date,
    min_value=min_date,
    max_value=max_date,
    help="Select the start date for filtering"
)

end_date = st.sidebar.date_input(
    "End Date",
    value=max_date,
    min_value=start_date,  # End date can't be before start date
    max_value=max_date,
    help="Select the end date for filtering"
)

# Get unique categories and cities
available_categories = sorted(df['category'].unique())
available_cities = sorted(df['city'].unique())

# Category filter with all options selected by default
selected_categories = st.sidebar.multiselect(
    "Select Categories",
    options=available_categories,
    default=available_categories,
    help="Choose product categories to display"
)

# City filter with all options selected by default
selected_cities = st.sidebar.multiselect(
    "Select Cities",
    options=available_cities,
    default=available_cities,
    help="Choose cities to display"
)

# Filter data
filtered_df = df[
    (df['date'].dt.date >= start_date) &
    (df['date'].dt.date <= end_date) &
    (df['category'].isin(selected_categories)) &
    (df['city'].isin(selected_cities))
]

# Main content
st.title("E-commerce Analytics Dashboard")

# Key metrics
metrics = calculate_key_metrics(filtered_df)
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Sales", metrics['total_sales'])
col2.metric("Total Orders", metrics['total_orders'])
col3.metric("Average Order Value", metrics['avg_order_value'])
col4.metric("Total Units Sold", metrics['total_units'])

# Charts
col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(create_sales_by_category_chart(filtered_df), use_container_width=True)
    st.plotly_chart(create_geographic_sales_chart(filtered_df), use_container_width=True)

with col2:
    st.plotly_chart(create_sales_trend_chart(filtered_df), use_container_width=True)
    st.plotly_chart(create_top_products_chart(filtered_df), use_container_width=True)

# Category performance
st.header("Category Performance")
for category in selected_categories:
    cat_data = filtered_df[filtered_df['category'] == category]
    col1, col2 = st.columns([1, 3])

    with col1:
        st.image(category_banners[category], use_container_width=True)

    with col2:
        st.subheader(category)
        metric1, metric2, metric3 = st.columns(3)
        cat_metrics = calculate_key_metrics(cat_data)
        metric1.metric("Category Sales", cat_metrics['total_sales'])
        metric2.metric("Category Orders", cat_metrics['total_orders'])
        metric3.metric("Category Units", cat_metrics['total_units'])

# Export data option
if st.button("Export Filtered Data"):
    csv = filtered_df.to_csv(index=False)
    st.download_button(
        label="Download CSV",
        data=csv,
        file_name="ecommerce_data.csv",
        mime="text/csv"
    )