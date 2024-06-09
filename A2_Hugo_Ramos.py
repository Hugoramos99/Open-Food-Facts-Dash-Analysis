#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 30 13:53:31 2024

@author: hugoramos
"""

import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
from dash import dash_table, html
from dash.dependencies import Input, Output, State

# Load the filtered CSV file
file_path = '/Users/hugoramos/Desktop/ESADE/3rd term/Prototyping/2nd assignment/open_food_facts_data.csv'  # Replace with your file path
df = pd.read_csv(file_path)

# Load the country counts data
country_counts = df['countries'].value_counts().reset_index()
country_counts.columns = ['country', 'number_of_products']

# Define a mapping dictionary for categories with multiple languages
category_mapping = {
    # Juices
    'fruit juices': 'Juices',
    'jus de fruits': 'Juices',
    'sucos de frutas': 'Juices',
    'jus': 'Juices',
    'juice': 'Juices',
    'succo': 'Juices',

    # Soft Drinks
    'sodas': 'Soft Drinks',
    'soft drinks': 'Soft Drinks',
    'boissons gazeuses': 'Soft Drinks',
    'refrescos': 'Soft Drinks',
    'gaseosas': 'Soft Drinks',
    'soda': 'Soft Drinks',
    'gazeuse': 'Soft Drinks',

    # Energy Drinks
    'energy drinks': 'Energy Drinks',
    'boissons énergisantes': 'Energy Drinks',
    'bebidas energéticas': 'Energy Drinks',
    'boisson énergisante': 'Energy Drinks',
    'energydrink': 'Energy Drinks',

    # Waters
    'waters': 'Waters',
    'water': 'Waters',
    'wasser': 'Waters',
    'eau': 'Waters',
    'agua': 'Waters',
    'acqua': 'Waters',

    # Coffees
    'coffees': 'Coffees',
    'cafés': 'Coffees',
    'café': 'Coffees',
    'kaffee': 'Coffees',

    # Milky Drinks
    'milky drinks': 'Milky Drinks',
    'boissons lactées': 'Milky Drinks',
    'bebidas lácteas': 'Milky Drinks',
    'milchgetränke': 'Milky Drinks',
    'milchhaltige getränke': 'Milky Drinks',
    'milchgetränk': 'Milky Drinks',
    'milch drink': 'Milky Drinks',

    # Vegetal Drinks
    'vegetal drinks': 'Vegetal Drinks',
    'boissons végétales': 'Vegetal Drinks',
    'bebidas vegetales': 'Vegetal Drinks',
    'pflanzliche getränke': 'Vegetal Drinks',

    # Alcohol
    'alcohol': 'Alcohol',
    'alcool': 'Alcohol',
    'bebidas alcohólicas': 'Alcohol',
    'alcoholic beverages': 'Alcohol',
    'boissons alcoolisées': 'Alcohol',
    'alcoholic drink': 'Alcohol',
    'alcoholisches getränk': 'Alcohol',
}


country_mapping = {
    # United States
    'États-Unis': 'United States',
    'Vereinigte Staaten': 'United States',
    'Estados Unidos': 'United States',
    'USA': 'United States',

    # Germany
    'Deutschland': 'Germany',
    'Allemagne': 'Germany',
    'Alemania': 'Germany',
    'germany':'Germany',
    'en:germany':'Germany',

    # Italy
    'Italia': 'Italy',
    'Italie': 'Italy',
    'Italien': 'Italy',

    # France
    'Francia': 'France',
    'Frankreich': 'France',
    'França': 'France',
    'france':'France',
    'en:france':'France',

    # Spain
    'España': 'Spain',
    'Spanien': 'Spain',

    # United Kingdom
    'United Kingdom': 'United Kingdom',
    'Reino Unido': 'United Kingdom',
    'Royaume-Uni': 'United Kingdom',
    'Großbritannien': 'United Kingdom',

    # Canada
    'Canada': 'Canada',
    'Kanada': 'Canada',

    # Australia
    'Australia': 'Australia',
    'Australie': 'Australia',
    'Australien': 'Australia',

    # Mexico
    'México': 'Mexico',
    'Mexiko': 'Mexico',

    # Japan
    '日本': 'Japan',
    'Japon': 'Japan',

    # China
    '中国': 'China',
    'Chine': 'China',

    # Brazil
    'Brasil': 'Brazil',
    'Brésil': 'Brazil',
    'Brasilien': 'Brazil',

    # Russia
    'Россия': 'Russia',
    'Russie': 'Russia',
    'Russland': 'Russia',

    # India
    'भारत': 'India',
    'Inde': 'India',

    # Netherlands
    'Nederland': 'Netherlands',
    'Países Bajos': 'Netherlands',
    'Pays-Bas': 'Netherlands',
    'Niederlande': 'Netherlands',

    # Belgium
    'Belgique': 'Belgium',
    'België': 'Belgium',
    'Bélgica': 'Belgium',

    # Switzerland
    'Suisse': 'Switzerland',
    'Schweiz': 'Switzerland',
    'Suiza': 'Switzerland',

    # Austria
    'Österreich': 'Austria',
    'Autriche': 'Austria',
    'Austria': 'Austria',

    # Sweden
    'Sverige': 'Sweden',
    'Suède': 'Sweden',
    'Suecia': 'Sweden',

    # Norway
    'Norge': 'Norway',
    'Norvège': 'Norway',
    'Noruega': 'Norway',

    # Finland
    'Suomi': 'Finland',
    'Finlande': 'Finland',
    'Finlandia': 'Finland',

    # Denmark
    'Danmark': 'Denmark',
    'Danemark': 'Denmark',
    'Dinamarca': 'Denmark',

    # Portugal
    'Portugal': 'Portugal',

    # Greece
    'Ελλάδα': 'Greece',
    'Grèce': 'Greece',
    'Grecia': 'Greece',

    # Poland
    'Polska': 'Poland',
    'Pologne': 'Poland',
    'Polonia': 'Poland',

    # Czech Republic
    'Česká republika': 'Czech Republic',
    'République tchèque': 'Czech Republic',
    'República Checa': 'Czech Republic',

    # Turkey
    'Türkiye': 'Turkey',
    'Turquie': 'Turkey',
    'Turquía': 'Turkey',

    # South Korea
    '대한민국': 'South Korea',
    'Corée du Sud': 'South Korea',
    'Corea del Sur': 'South Korea',

    # Argentina
    'Argentina': 'Argentina',
    'Argentine': 'Argentina',

    # Chile
    'Chile': 'Chile',
    'Chili': 'Chile',

    # South Africa
    'South Africa': 'South Africa',
    'Afrique du Sud': 'South Africa',
    'Südafrika': 'South Africa',
    'Sudáfrica': 'South Africa',
    
}
# Function to map detailed categories to broad categories
def map_category(category):
    category = category.lower()
    for key, value in category_mapping.items():
        if key in category:
            return value
    return 'Other'  # Default category for unmapped categories

# Function to clean and consolidate brand names
def clean_brand(brand):
    brand = brand.lower()
    if 'coca-cola' in brand or 'coca cola' in brand:
        if 'light' in brand:
            return 'Coca Cola Light'
        elif 'zero' in brand:
            return 'Coca Cola Zero'
        else:
            return 'Coca Cola'
    return brand.title()

# Apply the mapping to create a new column for broad categories
df['broad_category'] = df['categories'].apply(map_category)
# Clean the brand names
df['cleaned_brands'] = df['brands'].apply(lambda x: clean_brand(str(x)))

def map_country(country):
    if not isinstance(country, str):
        return 'Unknown'
    country = country.strip()
    return country_mapping.get(country, country)

# Split the 'countries' column into individual country names, map them, and count them properly
df['countries'] = df['countries'].str.split(',')
df['countries'] = df['countries'].apply(lambda x: [map_country(c) for c in x if isinstance(c, str)] if isinstance(x, list) else ['Unknown'])
country_counts = df.explode('countries')['countries'].value_counts().reset_index()
country_counts.columns = ['country', 'number_of_products']

# Filter out 'Unknown' countries
country_counts = country_counts[country_counts['country'] != 'Unknown']

# Count the number of additives per product
# Count the number of additives per product
df['additives_count'] = df['additives_tags'].apply(lambda x: len(str(x).split(',')) if pd.notna(x) else 0)

# Bin the additives count
bins = [0, 1, 2, 3, 4, float('inf')]
labels = ['0', '1', '2', '3', '4 & more']
df['additives_binned'] = pd.cut(df['additives_count'], bins=bins, labels=labels, right=False)

# Generate the heatmap data
heatmap_data = df.groupby(['broad_category', 'additives_binned']).size().unstack().fillna(0)


# Initialize the Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.FLATLY], suppress_callback_exceptions=True)

# Define a common title style
title_style = {
    'textAlign': 'center',
    'color': '#333',
    'fontSize': '32px',
    'fontWeight': 'bold'
}


# Calculate the color scale range
max_products = country_counts['number_of_products'].max()
color_scale_range = [0, max_products]

# Calculate the color scale range
max_products = country_counts['number_of_products'].max()
color_scale_range = [0, max_products]

paragraph_style = {
    'textAlign': 'center',
    'color': '#2c3e50',
    'fontSize': '18px'
}

# Define the layout for the home page
home_page = html.Div([
    html.Img(src='/assets/openfoodfacts_logo.png', style={'position': 'absolute', 'top': '20px', 'left': '20px', 'width': '50px', 'height': '50px'}),
    html.Div([
        html.H1("Welcome to the Nutritional Analysis Dashboard", style=title_style),
        html.P("This dashboard provides a comprehensive analysis of beverage products from the Open Food Facts database.", style=paragraph_style),
        html.P(f"The dataset contains information on {len(df)} beverage products, focusing on various nutritional aspects.", style=paragraph_style),
        html.P(["Data Source: ", html.A("Open Food Facts", href="https://world.openfoodfacts.org/cgi/search.pl", target="_blank", style=paragraph_style)], style=paragraph_style),
        html.P("Data was collected randomly through the API of the above website. In our data sample, most product are present in the French Market.", style=paragraph_style),
        html.P("In the below graph you can see the distribution of the products on the map", style=paragraph_style),
        html.P("Click on the Analysis Page to find out more insights !!", style=paragraph_style),
        dcc.Graph(
            id='world-map',
            figure=go.Figure(
                data=go.Choropleth(
                    locations=country_counts['country'],
                    locationmode='country names',
                    z=country_counts['number_of_products'],
                    colorscale='Viridis',
                    marker_line_color='darkgray',
                    marker_line_width=0.5,
                    showscale=False  # This line removes the color scale bar
                ),
                layout=go.Layout(
                    title='Number of Products Present by Country',
                    geo=dict(showframe=False, showcoastlines=True, projection_type='equirectangular')
                )
            )
        ),
        html.P("This dashboard is made in purpose of my Master in Business Analytics in the class Prototyping.", style=paragraph_style),
        html.P([
            "For every Query you can contact me at: ",
            html.A("Linkedin", href="https://www.linkedin.com/in/hugo-christophe-ramos", target="_blank"),
            " & ",
            html.A("Github", href="https://github.com/Hugoramos99", target="_blank")
        ], style=paragraph_style),
    ]),
    html.Div([
        dbc.NavLink("Go to Analysis Page", href="/analysis", external_link=True, className="btn btn-primary")
    ], style={'position': 'absolute', 'top': '20px', 'right': '20px'})  # Adjust the position here
])




#Heatmap
heatmap_fig = px.imshow(
    heatmap_data,
    labels=dict(x="Number of Additives", y="Category", color="Count"),
    aspect="auto",
    color_continuous_scale=[(0, "white"), (1, "red")]
)

heatmap_fig.update_layout(
    title=dict(
        text='Heatmap of Categories vs Number of Additives',
        font=dict(size=24),  # Set the font size
        y=0.95,
        x=0.5,
        xanchor='center',
        yanchor='top'
    )
)


# Define the layout for the analysis page
analysis_page = html.Div([
    html.Img(src='/assets/openfoodfacts_logo.png', style={'position': 'absolute', 'top': '20px', 'left': '20px', 'width': '50px', 'height': '50px'}),
    html.Div([
        html.H1("Nutritional Analysis of Drinks", style=title_style),
        html.P("On this page you can see several graphs offering insights on the different Drink Product Categories.", style=paragraph_style),
        html.P("Small tip : You can click on one of the category to filter the other graphs !!.", style=paragraph_style),
        dcc.Graph(id='category-nutriscore-distribution'),
        html.Button("Clear Selection", id="clear-selection-button", n_clicks=0, className="btn btn-primary"),
        dcc.Graph(id='brand-sugar-products'),
        html.Div(id='top-10-healthiest', style={'marginBottom': '50px'}),
        html.Div(id='top-10-unhealthiest', style={'marginBottom': '50px'}),
        dcc.Graph(id='heatmap', figure=heatmap_fig),  # Add heatmap here
    ]),
    html.Div([
        dbc.NavLink("Go to Home Page", href="/", external_link=True, className="btn btn-secondary")
    ], style={'position': 'absolute', 'top': '20px', 'right': '20px'})  # Adjust the position here
])

# Define the app layout with multi-page support
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

# Callback to control page navigation
@app.callback(Output('page-content', 'children'), [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/analysis':
        return analysis_page
    else:
        return home_page

@app.callback(
    [
        Output('brand-sugar-products', 'figure'),
        Output('top-10-healthiest', 'children'),
        Output('top-10-unhealthiest', 'children'),
        Output('category-nutriscore-distribution', 'figure'),  # Change here
    ],
    [Input('category-nutriscore-distribution', 'clickData'),
     Input('clear-selection-button', 'n_clicks')],
    [State('category-nutriscore-distribution', 'clickData')]
)
def update_graphs(click_data, n_clicks, state_click_data):
    ctx = dash.callback_context

    if not ctx.triggered:
        button_id = 'No clicks yet'
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if button_id == "clear-selection-button":
        filtered_df = df
    elif click_data:
        selected_category = click_data['points'][0]['x']
        filtered_df = df[df['broad_category'] == selected_category]
    else:
        filtered_df = df


    # Check if filtered_df is empty
    if filtered_df.empty:
        print("Filtered DataFrame is empty.")
        # Return empty figures and tables
        empty_fig = go.Figure()
        empty_table = html.Div([])
        return empty_fig, empty_table, empty_table, empty_fig

    
   # Brand vs. number of products and sugar content
    brand_sugar_products = filtered_df.groupby('cleaned_brands').agg(
        number_of_products=('product_name', 'count'),
        avg_sugar=('sugars_100g', 'mean')
    ).reset_index()
    brand_sugar_products = brand_sugar_products[brand_sugar_products['number_of_products'] > 1]
    brand_sugar_products_fig = px.scatter(
        brand_sugar_products, x='number_of_products', y='avg_sugar', color='cleaned_brands', 
        size='number_of_products', title='Brands: Number of Products vs. Average Sugar Content'
    )
    brand_sugar_products_fig.update_layout(
        title=dict(
            text='Number of products per Brands compared with amount of Suga',
            font=dict(size=24),
            y=0.95,
            x=0.5,
            xanchor='center',
            yanchor='top'
        )
    )

    # Top 5 healthiest drinks based on NutriScore, sugar content, and fat content
    healthiest_drinks = filtered_df.sort_values(by=['nutriscore_grade', 'sugars_100g', 'fat_100g']).head(5)
    healthiest_table = html.Div([
        html.H2("Top 5 Healthiest Drinks"),
        dash_table.DataTable(
            columns=[{"name": i, "id": i} for i in healthiest_drinks[['product_name', 'nutriscore_grade', 'sugars_100g', 'fat_100g']].columns],
            data=healthiest_drinks[['product_name', 'nutriscore_grade', 'sugars_100g', 'fat_100g']].to_dict('records'),
            style_table={'overflowX': 'auto'},
            style_cell={'textAlign': 'left'},
        ),
        html.Br()  # Add space between tables
    ])

    # Top 5 unhealthiest drinks based on sugar content
    unhealthiest_drinks = filtered_df.nlargest(5, 'sugars_100g')
    unhealthiest_table = html.Div([
        html.H2("Top 5 Unhealthiest Drinks"),
        dash_table.DataTable(
            columns=[{"name": i, "id": i} for i in unhealthiest_drinks[['product_name', 'nutriscore_grade', 'sugars_100g', 'fat_100g']].columns],
            data=unhealthiest_drinks[['product_name', 'nutriscore_grade', 'sugars_100g', 'fat_100g']].to_dict('records'),
            style_table={'overflowX': 'auto'},
            style_cell={'textAlign': 'left'},
        ),
        html.Br()  # Add space between tables
    ])

    # Number of products per broad category
    category_counts = df['broad_category'].value_counts().reset_index()
    category_counts.columns = ['broad_category', 'counts']
    category_nutriscore_fig = px.bar(
        category_counts, x='broad_category', y='counts', title='Number of Products per Category'
    )
    category_nutriscore_fig.update_layout(
        title=dict(
            text='Number of Products per Category',
            font=dict(size=24),
            y=0.95,
            x=0.5,
            xanchor='center',
            yanchor='top'
        )
    )
    

    
    return brand_sugar_products_fig, healthiest_table, unhealthiest_table, category_nutriscore_fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True, port=8052)




