import streamlit as st
import requests
from bs4 import BeautifulSoup
import json
from inference import run_inference

def scrape_amazon(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup.find_all("span", class_="a-list-item")
    elif response.status_code == 403:
        print("Request was blocked by Amazon. Consider changing your IP or User-Agent.")
    elif response.status_code == 429:
        print("Rate limit exceeded. Try slowing down your requests.")
    else:
        print(f"Unhandled status code: {response.status_code}")
    return None


def scrape_amazon(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    print("Status Code:", response.status_code)
    print("Headers:", response.headers)
    print("Response Body (first 500 chars):", response.text[:500])
    if response.status_code != 200:
        return None
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.find_all("span", class_="a-list-item")


def main():
    st.title("Product Score Analyzer")
    amazon_url = st.text_input("Enter the Amazon product URL:")

    if st.button("Analyze Sustainability Score"):
        if amazon_url:
            list_items = scrape_amazon(amazon_url)
            if not list_items:
                st.error("Failed to fetch data from Amazon. Please check the URL or try again later.")
                return

            get_image = scrape_amazon_image(amazon_url)
            texts = [item.get_text(strip=True) for item in list_items]
            concatenated_text = " ".join(texts)

            prompt = f"""
            only response in json format like {{esg_score : 'value(0-100)' }} sample:
            {{
                "esg_score": "60",
                ...
            }}
            that is the sustainability score of this content :
            analysis this : 
            {concatenated_text}
            """

            try:
                response = run_inference(prompt)
                st.write("Debug: Response from run_inference", response)
                response_dict = json.loads(response)
                st.image(get_image, caption='Product Image', width=200)
                st.header('Sustainability Score: ')
                st.write(response_dict['esg_score'])
                st.header('Pros: ')
                for key, value in response_dict['pros'].items():
                    st.write(f'{key}. {value}')
                st.header('Cons: ')
                for key, value in response_dict['cons'].items():
                    st.write(f'{key}. {value}')
            except Exception as e:
                st.error(f"An error occurred: {e}")
        else:
            st.error("Please enter a valid Amazon product URL.")

if __name__ == "__main__":
    main()
