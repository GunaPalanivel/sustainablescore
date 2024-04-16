import streamlit as st

def display_topic_information():
    st.markdown("""
    ## Sustainability
    Sustainability involves meeting present needs without compromising the ability of future generations to meet their own needs, focusing on environmental, social, and economic balance and responsibility.

    ## Lungs Fractal
    The Lungs Fractal is a unique air purification system inspired by the intricate patterns found in nature, designed to enhance indoor air quality and promote a healthier living environment.
                
    ## Product Usage
    Sustainable product usage emphasizes minimizing resource consumption, reducing waste, and promoting long-term environmental stewardship throughout the product's lifecycle.
                
    ## San Francisco Green Business
    San Francisco Green Business certification recognizes businesses that demonstrate environmental leadership by adopting sustainable practices and reducing their ecological footprint in the city.

    ## Gross Income (Sustainability)
    The gross income of a business represents the total revenue generated before deducting any expenses, taxes, or other costs associated with operations.
    """)

def main():
    st.title("Let's Know More About Sustainability")
    display_topic_information()

if __name__ == "__main__":
    main()
