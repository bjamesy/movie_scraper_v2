import requests
from bs4 import BeautifulSoup
# from pyppeteer import launch

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

# async def get_tiff():
#     # tiff calendar page
#     url = "https://tiff.net/calendar"

#     browser = await launch()
#     page = await browser.newPage()
#     await page.goto(url)

#     screenings = await page.evaluate('''() => {
#         return {
#             width: document.documentElement.clientWidth,
#             height: document.documentElement.clientHeight,
#             deviceScaleFactor: window.devicePixelRatio,
#         }
#     }''')

#     print("SCREENINGS", screenings)

#     return screenings

#     await browser.close()

async def get_fox():
    # fox calendar page
    url = "https://www.foxtheatre.ca/schedule/"

    response = requests.get(url)

    if response.status_code == 200:
        screenings = []

        html = BeautifulSoup(response.text, 'html.parser')
        todays_movies = html.find(class_="fc-day-today")

        movies = todays_movies.find_all(class_="fc-daygrid-event-harness")

        for movie in movies:
            screenings.append({
                "title": movie.find(class_="fc-event-title").text,
                "time": movie.find(class_="fc-event-time").text,
                "link": movie.find(class_='fc-event-today')['href']
            })

        print("SCREENINGS", screenings)

        return screenings
    else:
        print(f"Fox Error: {response.status_code}")

        return False

async def get_carlton():
    # carlton calendar page
    url = "https://imaginecinemas.com/cinema/carlton/"

    response = requests.get(url)

    if response.status_code == 200:
        screenings = []
        showtimes = []

        html = BeautifulSoup(response.text, 'html.parser')
        movies = html.find(id="theater-schedule").find_all(class_="movie-showtime")

        for movie in movies:
            times = movie.find(class_='times').find_all(class_='movie-performance')
            for time in times:
                showtimes.append(time.text)

            screenings.append({
                "title": movie.find(class_="movie-title").text,
                "time": showtimes,
                "link": movie.find(class_='movie-poster').find('a')['href']
            })
            showtimes = []

        print("SCREENINGS", screenings)

        return screenings
    else:
        print(f"Carlton Error: {response.status_code}")

        return False

async def get_paradise():
    # paradise calendar page
    url = "https://paradiseonbloor.com/calendar"

    response = requests.get(url)

    if response.status_code == 200:
        screenings = []

        html = BeautifulSoup(response.text, 'html.parser')
        movies = html.find(class_="current-day").find_all(class_="calendar-event")

        for movie in movies:
            screenings.append({
                "title": movie.find(class_="event-title").text,
                "time": movie.find(class_="event-date-time").text,
                "link": movie.find(class_='event-links').find('a')['href']
            })

        print("SCREENINGS", screenings)

        return screenings
    else:
        print(f"Paradise Error: {response.status_code}")

        return False