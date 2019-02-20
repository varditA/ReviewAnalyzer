from selenium import webdriver
from bs4 import BeautifulSoup
import time

categories_names = ["GAME_ACTION", "GAME_ADVENTURE", "GAME_ARCADE", "GAME_BOARD", "GAME_CARD",
                    "GAME_CASINO", "GAME_CASUAL", "GAME_EDUCATIONAL", "GAME_MUSIC", "GAME_PUZZLE",
                    "GAME_RACING", "GAME_ROLE_PLAYING", "GAME_SIMULATION", "GAME_SPORTS", "GAME_STRATEGY"]


# def getReviews(appsDict, appsList):
#     apps_urls = set()
#     url = 'https://play.google.com/store/apps/collection/recommended_for_you?clp=ogoKCAEqAggBUgIIAQ%3D%3D:S:ANO1ljJG6Aw&gsr=Cg2iCgoIASoCCAFSAggB:S:ANO1ljLKNqE'
#     # setting up connection, get the info and closing it
#     driver = webdriver.Chrome()
#     driver.implicitly_wait(30)
#     driver.get(url)
#
#     html_soup = BeautifulSoup(driver.page_source, 'lxml')
#     # html_soup.findAll('div', {"class": "card no-rationale square-cover apps small"})
#     for link in html_soup.findAll('div', {"class": "card no-rationale square-cover apps small"}):
#         href = link.a.get("href")
#         apps_urls.add("https://play.google.com" + href)
#
#     #get apps reviews
#     for app_url in apps_urls:
#         driver.implicitly_wait(30)
#         time.sleep(2)
#         driver.get(app_url + "&showAllReviews=true")
#         try:
#             new_soup = BeautifulSoup(driver.page_source, 'lxml')
#         except:
#             continue
#         app_title = (new_soup.find('h1', {"class": "AHFaub"})).text
#         appsList.append(app_title)
#         span = new_soup.findAll('span', jsname="bN97Pc")
#         reviews = []
#         for s in span:
#             reviews.append(s.text)
#         appsDict[app_title] = reviews
#         print(appsList)
#
#     driver.close()
#     with open('reviews.txt', 'w') as outfile:
#         json.dump(appsDict, outfile)


def getReviews(appsDict, appsList):
    # categories = set()
    apps_urls = set()

    # setting up connection, get the info and closing it
    driver = webdriver.Chrome('modules/chromedriver.exe')
    driver.implicitly_wait(30)

    # url = "https://play.google.com/store"
    # driver.get(url)
    # html_soup = BeautifulSoup(driver.page_source, 'lxml')

    # get the categories urls
    # for link in html_soup.findAll('li', {"class": "child-submenu-link-wrapper"}):
    #     href = link.a.get("href")
    #     categories.add("https://play.google.com" + href)
    # print(len(categories))

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
        # print(len(apps_urls))

    for app_url in apps_urls:
        driver.implicitly_wait(30)
        time.sleep(2)
        driver.get(app_url + "&showAllReviews=true")
        try:
            soup2 = BeautifulSoup(driver.page_source, 'lxml')
        except:
            continue
        app_title = (soup2.find('h1', {"class": "AHFaub"})).text
        # print(app_title)
        appsList.add(app_title)
        span = soup2.findAll('span', jsname="bN97Pc")
        reviews = []
        for s in span:
            reviews.append(s.text)
        appsDict[app_title] = reviews

    driver.close()


