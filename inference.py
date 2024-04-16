import requests
import json
import os  # For accessing environment variables securely

def run_inference(prompt):
    # Retrieve the API key stored in an environment variable
    api_key = os.getenv("GEMINI_API_KEY")  # Ensure that GEMINI_API_KEY is set in your environment variables
    if not api_key:
        raise ValueError("API key not found in environment variables")

    url = 'https://api.gemini.com/v1/inference'  # Update with the actual inference API URL provided by Gemini
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'  # Use the API key
    }

    data = {
        "prompt": prompt,
        "parameters": {
            "max_tokens": 512,
            "temperature": 0.7
        }
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # Raise an exception for HTTP error responses
        return response.json()  # Return the JSON response
    except requests.exceptions.HTTPError as errh:
        return f"HTTP Error: {errh}"
    except requests.exceptions.ConnectionError as errc:
        return f"Connection Error: {errc}"
    except requests.exceptions.Timeout as errt:
        return f"Timeout Error: {errt}"
    except requests.exceptions.RequestException as err:
        return f"Error: {err}"
    except json.JSONDecodeError:
        return "Error parsing JSON: " + response.text

# Example usage of the function
if __name__ == "__main__":
    test_prompt = "Analyze the sustainability of this product."
    result = run_inference(test_prompt)
    print(result)
