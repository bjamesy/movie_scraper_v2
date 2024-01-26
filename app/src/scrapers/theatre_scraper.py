import requests
from bs4 import BeautifulSoup
import pyppeteer
from pyppeteer import launch

pyppeteer.DEBUG = True  # print suppressed errors as error log

def get_revue():
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
    # tiff calendar page
    url = "https://tiff.net/calendar"

    browser = await launch(executablePath='/usr/bin/google-chrome-stable', headless=True, args=['--no-sandbox'])
    page = await browser.newPage()
    await page.goto(url)
    # await page.waitForSelector('.0', {'visible': True})
    html = await page.content()

    await browser.close()

    screenings = []
    showtimes = []

    soup = BeautifulSoup(html, 'html.parser')
    todays_movies = soup.find(class_="0")
    movies = todays_movies.find_all(class_="style__resultCard___vLGmu")

    for movie in movies:
        times = movie.find_all(class_='style__screeningButton___3rUW8')
        print(times)
        for time in times:
            showtimes.append(time.text)

        screenings.append({
            "title": movie.find(class_="style__cardTitle___3rkLd").text,
            "time": showtimes,
            "link": f"tiff.net{movie.find(class_='row style__cardScheduleItems___36bhs').find('a')['href']}"
        })

        showtimes = []

    print("SCREENINGS", screenings)

    return screenings


async def get_fox():
    # fox calendar page
    url = "https://www.foxtheatre.ca/schedule/"

    browser = await launch(executablePath='/usr/bin/google-chrome-stable', headless=True, args=['--no-sandbox'])
    page = await browser.newPage()
    await page.goto(url)
    # await page.waitForSelector('.fc-daygrid-day-events', {'visible': True})
    html = await page.content()

    await browser.close()

    screenings = []

    soup = BeautifulSoup(html, 'html.parser')
    todays_movies = soup.find(class_="fc-media-screen")
    movies = todays_movies.find_all(class_="fc-event-today")

    for movie in movies:
        screenings.append({
            "title": movie.find(class_="fc-list-event-title").text,
            "time": movie.find(class_="fc-list-event-time").text,
            "link": movie.find('a')['href']
        })

    print("SCREENINGS", screenings)

    return screenings


def get_carlton():
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


def get_paradise():
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


def get_kingsway():
    # kingsway calendar page
    url = "http://kingswaymovies.ca/index.html"

    response = requests.get(url)

    if response.status_code == 200:
        screenings = []

        html = BeautifulSoup(response.text, 'html.parser')
        movies = html.find_all(style="border: 2px solid ; width: 630px; height: 198px;")

        for movie in movies:
            screenings.append({ movie['alt'] })

        print("SCREENINGS", screenings)

        return screenings
    else:
        print(f"Kingsway Error: {response.status_code}")

        return False

    
async def get_hotdocs():
    # kingsway calendar page
    url = "https://hotdocs.ca/whats-on/watch-cinema"

    browser = await launch(executablePath='/usr/bin/google-chrome-stable', headless=True, args=['--no-sandbox'])
    page = await browser.newPage()
    await page.goto(url)
    # await page.waitForSelector('.fc-daygrid-day-events', {'visible': True})
    html = await page.content()

    await browser.close()

    screenings = []

    soup = BeautifulSoup(html, 'html.parser')

    movies = soup.find(class_='cinema-day').find_all(class_='film-tote')

    for movie in movies:
        screenings.append({
            "title": movie.find(class_="film-tote__heading").text,
            "time": movie.find(class_="ticket-strip__time").text,
            "link": movie.find(class_='ticket-strip')['href']
        })

    print("SCREENINGS", screenings)

    return screenings