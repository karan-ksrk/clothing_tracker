import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_mock_data():
    # Product categories
    categories = ['T-Shirts', 'Jeans', 'Dresses', 'Shirts', 'Sweaters']

    # Product data
    products = {
        'T-Shirts': [
            ('Classic White Tee', 'https://images.unsplash.com/photo-1602810318383-e386cc2a3ccf'),
            ('Black Essential Tee', 'https://images.unsplash.com/photo-1603252110971-b8a57087be18'),
        ],
        'Jeans': [
            ('Blue Slim Fit', 'https://images.unsplash.com/photo-1479064555552-3ef4979f8908'),
            ('Black Straight Cut', 'https://images.unsplash.com/photo-1535486648131-54a1558cb3fc'),
        ],
        'Dresses': [
            ('Summer Floral', 'https://images.unsplash.com/photo-1523381294911-8d3cead13475'),
            ('Evening Black', 'https://images.unsplash.com/photo-1529374255404-311a2a4f1fd9'),
        ],
        'Shirts': [
            ('Business White', 'https://images.unsplash.com/photo-1603252109360-909baaf261c7'),
            ('Casual Blue', 'https://images.unsplash.com/photo-1603252109612-24fa03d145c8'),
        ],
        'Sweaters': [
            ('Wool Knit', 'https://images.unsplash.com/photo-1603370928866-e15805756740'),
            ('Cardigan', 'https://images.unsplash.com/photo-1603251578711-3290ca1a0187'),
        ]
    }

    # Locations
    cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Miami', 
              'Seattle', 'Boston', 'San Francisco', 'Dallas', 'Denver']

    # Generate sales data
    data = []
    start_date = datetime.now() - timedelta(days=365)

    for _ in range(10000):  # Generate 10000 sales records
        category = np.random.choice(categories)
        product_info = products[category]
        idx = np.random.randint(0, len(product_info))
        product_name, image_url = product_info[idx]
        city = np.random.choice(cities)
        date = start_date + timedelta(days=np.random.randint(0, 365))
        quantity = np.random.randint(1, 10)
        price = np.random.uniform(20, 200)

        data.append({
            'date': date,
            'category': category,
            'product_name': product_name,
            'image_url': image_url,
            'city': city,
            'quantity': quantity,
            'price': price,
            'total_sales': quantity * price
        })

    df = pd.DataFrame(data)
    return df

def get_category_banners():
    return {
        'T-Shirts': 'https://images.unsplash.com/photo-1483985988355-763728e1935b',
        'Jeans': 'https://images.unsplash.com/photo-1490481651871-ab68de25d43d',
        'Dresses': 'https://images.unsplash.com/photo-1484327973588-c31f829103fe',
        'Shirts': 'https://images.unsplash.com/photo-1506152983158-b4a74a01c721',
        'Sweaters': 'https://images.unsplash.com/photo-1558769132-cb1aea458c5e'
    }