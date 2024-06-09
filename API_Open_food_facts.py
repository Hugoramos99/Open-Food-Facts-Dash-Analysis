#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 30 13:38:46 2024

@author: hugoramos
"""

import requests
import pandas as pd
import os

# Define the API endpoint and parameters
api_url = "https://world.openfoodfacts.org/cgi/search.pl"
parameters = {
    "tagtype_0": "categories",
    "tag_contains_0": "contains",
    "tag_0": "drinks",
    "fields": "product_name,brands,countries,categories,nutriscore_grade,energy_100g,fat_100g,saturated-fat_100g,sugars_100g,salt_100g,proteins_100g,fiber_100g,carbohydrates_100g,ingredients_text,additives_tags,ecoscore_grade,packaging,packaging_tags,origins,manufacturing_places,stores,labels",
    "search_simple": 1,
    "action": "process",
    "json": 1,
    "page_size": 100,  # Adjust the number of records per request
    "page": 1         # Start with the first page
}

# Function to fetch data from the API
def fetch_data(api_url, parameters):
    response = requests.get(api_url, params=parameters)
    if response.status_code == 200:
        data = response.json()
        return data['products']
    else:
        print(f"Failed to retrieve data: {response.status_code}")
        return []

# Fetch data
all_products = []
for page in range(1, 35):  # Adjust the range to fetch more pages
    print(f"Fetching page {page}")
    parameters['page'] = page
    products = fetch_data(api_url, parameters)
    if not products:
        break
    all_products.extend(products)

# Convert the data to a Pandas DataFrame
df = pd.DataFrame(all_products)

# Display the DataFrame
print(df.head())


# Save the DataFrame to a CSV file
df.to_csv('open_food_facts_data.csv', index=False)
