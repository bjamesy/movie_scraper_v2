import requests
from bs4 import BeautifulSoup

async def get_revue():
    # URL of the website you want to scrape
    url = "https://revuecinema.ca/"

    # Send a GET request to the URL
    response = requests.get(url)

    print("Tentative response ....", response)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        print("IN HERE : ")
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')
        print("HERE", soup)
        print("Here is the DOM: ", soup)

        # Extract information based on the structure of the HTML
        # For example, let's extract movie titles from h2 elements
        # movie_titles = [h2.text.strip() for h2 in soup.find_all('h2')]

        # Print the extracted movie titles
        # for title in movie_titles:
        #     print(title)

        
        return True
    else:
        print(f"Revue Error: {response.status_code}")

        return False

