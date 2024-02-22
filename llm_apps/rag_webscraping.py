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
    
    # Find all term names - adjust the tag and class based on actual structure
    term_names = soup.find_all('dt', class_='term-item svelte-po9bzm')
    
    # Initialize a list to hold term names and descriptions
    terms_data = []
    
    # Loop through each term name
    for term_name in term_names:
        # Extract the text of the term name
        name_text = term_name.find('dfn').get_text(strip=True)
        
        # Find the next sibling of `dt` which should be `dd` containing the description
        description = term_name.find_next_sibling('dd', class_='term-item svelte-po9bzm')
        description_text = description.get_text(strip=True) if description else ""
        description_text = f"{name_text} {description_text}"
        # Append the name and description as a row in the list
        terms_data.append([description_text])
    
    # Create a DataFrame
    df = pd.DataFrame(terms_data, columns=['Description'])
    
    # Save the DataFrame to a CSV file
    df.to_csv('economics_terms.csv', index=False)
    
    print("CSV file has been created successfully.")
else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)
