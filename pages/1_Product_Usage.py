import streamlit as st
import numpy as np
import plotly.graph_objects as go
import pandas as pd
import plotly.io as pio

def sustainability_product_usage_graph():
    st.set_page_config(page_title="Sustainability Product Usage", page_icon="🌍")
    st.markdown("# Sustainability Product Usage")
    st.sidebar.header("Sustainability Product Usage")
    st.write(
        """This graph illustrates the usage of a sustainability product worldwide. The color intensity of each country represents the product usage."""
    )

    # Create a sample dataframe for product usage
    product_usage_data = pd.DataFrame({
        'country': ['USA', 'Canada', 'Mexico', 'Brazil', 'Argentina', 'Chile', 'France', 'Germany'],
        'usage': [20, 30, 15, 25, 35, 10, 40, 28]
    })

    # Create a Choropleth map using Plotly
    fig = go.Figure(go.Choropleth(
        locations=product_usage_data['country'],
        z=product_usage_data['usage'],
        locationmode='country names',
        colorscale='Viridis',
        colorbar_title='Usage',
    ))

    fig.update_layout(
        title_text='Sustainability Product Usage Worldwide',
        geo=dict(
            showcoastlines=True,
        )
    )

    st.plotly_chart(fig)

# Call the function to display the graph
sustainability_product_usage_graph()