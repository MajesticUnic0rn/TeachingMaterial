## let me first scrap the data 

import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the page to scrape
url = "https://www.economist.com/economics-a-to-z"

# Send a GET request to the page
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the content of the request with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all term elements - you might need to update the selector based on actual page structure
    terms = soup.find_all('dd', class_='term-item svelte-po9bzm') # This is a placeholder, adjust the tag and class based on actual structure
    
    # Create a list to hold our term texts
    term_texts = []
    
    # Loop through each term and extract the text
    for term in terms:
        term_text = term.get_text(strip=True)
        term_texts.append([term_text]) # Append as a list to create a row for each term
    
    # Create a DataFrame
    df = pd.DataFrame(term_texts, columns=['Term'])
    
    # Save the DataFrame to a CSV file
    df.to_csv('economics_terms.csv', index=False)
    
    print("CSV file has been created successfully.")
else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)
