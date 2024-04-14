# Product Sustainability Analyzer

# Built for [GreenLexicon](https://github.com/GunaPalanivel/GreenLexicon.git)

## Overview

The Product Sustainability Analyzer is a Streamlit web application that allows users to analyze the sustainability of products listed on Amazon. The application scrapes the product page, extracts relevant information, and sends it to an AI-powered backend to generate a comprehensive sustainability analysis. The analysis includes an overall sustainability score, as well as a list of pros and cons related to the product's environmental impact.

## Features

1. **Amazon Product URL Input**: Users can enter the URL of an Amazon product they want to analyze.
2. **Sustainability Score**: The application calculates and displays a sustainability score for the product, ranging from 0 to 100, with higher scores indicating more sustainable products.
3. **Pros and Cons**: The application provides a detailed list of the product's pros and cons in terms of sustainability, helping users make informed purchasing decisions.
4. **Product Image**: The application attempts to fetch and display the product's image, providing a visual representation of the item.

## Usage

1. **Set up the Development Environment**:
   - You can use the provided development container configuration to set up the development environment with the necessary dependencies.
   - Alternatively, you can create a virtual environment and install the required packages manually.

2. **Run the Application**:
   - Start the Streamlit server by running the following command in your terminal:
     ```
     streamlit run Hello.py
     ```
   - The application will open in your default web browser.

3. **Analyze a Product**:
   - In the application, enter the URL of the Amazon product you want to analyze.
   - Click the "Analyze Sustainability Score" button to initiate the analysis.
   - The application will display the product's sustainability score, as well as a list of pros and cons related to its environmental impact.

## Dependencies

The application relies on the following Python libraries:

- `streamlit`: For building the web application.
- `requests`: For sending HTTP requests to scrape the Amazon product page.
- `BeautifulSoup`: For parsing the HTML content of the Amazon product page.
- `inference`: For sending the scraped content to the AI-powered backend and retrieving the sustainability analysis.

These dependencies are listed in the `requirements.txt` file, which can be used to install the necessary packages.

## Customization

You can customize the application by modifying the following elements:

1. **Scraping Logic**: The `scrape_amazon()` and `scrape_amazon_image()` functions can be modified to adapt to changes in the Amazon product page structure.
2. **API Integration**: The `run_inference()` function in the `inference.py` file can be updated to integrate with your preferred AI-powered backend for generating the sustainability analysis.
3. **User Interface**: You can further customize the Streamlit-based user interface, such as the page title, layout, and styling, to match your branding and preferences.

## License

This project is licensed under the [Apache License, Version 2.0](LICENSE).
