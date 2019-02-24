from selenium import webdriver
from bs4 import BeautifulSoup
import time

categories_names = ["GAME_ACTION", "GAME_ADVENTURE", "GAME_ARCADE", "GAME_BOARD", "GAME_CARD",
                    "GAME_CASINO", "GAME_CASUAL", "GAME_EDUCATIONAL", "GAME_MUSIC", "GAME_PUZZLE",
                    "GAME_RACING", "GAME_ROLE_PLAYING", "GAME_SIMULATION", "GAME_SPORTS", "GAME_STRATEGY"]


def getReviews(appsDict, appsList):
    apps_urls = set()

    # setting up connection, get the info and closing it
    driver = webdriver.Chrome('modules/chromedriver.exe')
    driver.implicitly_wait(30)

    # get the apps urls
    for category in categories_names:
        driver.implicitly_wait(30)
        time.sleep(2)
        driver.get("https://play.google.com/store/apps/category/" + category)
        try:
            soup1 = BeautifulSoup(driver.page_source, 'lxml')
        except:
            continue
        for link in soup1.findAll('div', {"class": "card no-rationale square-cover apps small"}):
            href = link.a.get("href")
            apps_urls.add("https://play.google.com" + href)

    # get the reviews of each app
    for app_url in apps_urls:
        driver.implicitly_wait(30)
        time.sleep(2)
        driver.get(app_url + "&showAllReviews=true")
        last_height = driver.execute_script("return document.body.scrollHeight")
        while True:
            # Scroll down to bottom
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
        try:
            soup2 = BeautifulSoup(driver.page_source, 'lxml')
        except:
            continue
        app_title = (soup2.find('h1', {"class": "AHFaub"})).text
        span = soup2.findAll('span', jsname="bN97Pc")
        reviews = []
        for s in span:
            reviews.append(s.text)
        if len(reviews) >= 20:
            appsDict[app_title] = reviews
            appsList.add(app_title)
    print("num of apps: ", str(len(appsDict)))
    driver.close()
