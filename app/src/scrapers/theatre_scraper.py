import requests
from bs4 import BeautifulSoup
from selenium import webdriver

async def get_revue():
    # revue calendar page
    url = "https://prod3.agileticketing.net/websales/pages/list.aspx?epguid=9416d3bf-ad16-479c-9d40-f0abda7cb4e9&"

    response = requests.get(url)

    if response.status_code == 200:
        screenings = []

        html = BeautifulSoup(response.text, 'html.parser')
        todays_movies = html.find(class_="InsideDate Current")
        movies = todays_movies.find_all(class_="Item")

        for movie in movies:
            screenings.append({
                "title": movie.find(class_="Name").text,
                "time": movie.find(class_="Time").text,
                "link": f"prod3.agileticketing.net/websales/pages/{movie.find(class_='ButtonLink')['href']}"
            })

        print("SCREENINGS", screenings)

        return screenings
    else:
        print(f"Revue Error: {response.status_code}")

        return False

async def get_tiff():
    screenings = []
    # tiff calendar page
    url = "https://tiff.net/calendar"

    browser = webdriver.PhantomJS()
    browser.get(url)
    html = browser.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # todays_movies = html.find(class_="0").find_all('li')

    print("TODAYS MOVIES", soup.prettify())
    # for movie in todays_movies:
    #     movie
    #     screenings.append({
    #         "title": movie.find(class_="Name").text,
    #         "time": movie.find(class_="Time").text,
    #         "link": f"prod3.agileticketing.net/websales/pages/{movie.find(class_='ButtonLink')['href']}"
    #     })

    print("SCREENINGS", screenings)

    return screenings

