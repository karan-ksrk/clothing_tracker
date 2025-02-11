import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

def create_sales_by_category_chart(df):
    sales_by_category = df.groupby('category')['total_sales'].sum().reset_index()
    fig = px.pie(sales_by_category, values='total_sales', names='category',
                 title='Sales Distribution by Category')
    return fig

def create_sales_trend_chart(df):
    daily_sales = df.groupby('date')['total_sales'].sum().reset_index()
    fig = px.line(daily_sales, x='date', y='total_sales',
                  title='Daily Sales Trend')
    return fig

def create_top_products_chart(df):
    top_products = df.groupby('product_name')['total_sales'].sum().sort_values(
        ascending=False).head(10).reset_index()
    fig = px.bar(top_products, x='product_name', y='total_sales',
                 title='Top 10 Products by Sales')
    return fig

def create_geographic_sales_chart(df):
    sales_by_city = df.groupby('city')['total_sales'].sum().reset_index()
    fig = px.bar(sales_by_city, x='city', y='total_sales',
                 title='Sales by City')
    return fig

def format_currency(value):
    return f"${value:,.2f}"

def calculate_key_metrics(df):
    total_sales = df['total_sales'].sum()
    total_orders = len(df)
    avg_order_value = total_sales / total_orders
    total_units = df['quantity'].sum()
    
    return {
        'total_sales': format_currency(total_sales),
        'total_orders': f"{total_orders:,}",
        'avg_order_value': format_currency(avg_order_value),
        'total_units': f"{total_units:,}"
    }
