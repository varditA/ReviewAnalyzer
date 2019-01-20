from selenium import webdriver
from bs4 import BeautifulSoup
import time
import json


def getReviews(appsDict, appsList):
    apps_urls = set()
    url = 'https://play.google.com/store/apps/collection/recommended_for_you?clp=ogoKCAEqAggBUgIIAQ%3D%3D:S:ANO1ljJG6Aw&gsr=Cg2iCgoIASoCCAFSAggB:S:ANO1ljLKNqE'
    # setting up connection, get the info and closing it
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    driver.get(url)

    html_soup = BeautifulSoup(driver.page_source, 'lxml')
    # html_soup.findAll('div', {"class": "card no-rationale square-cover apps small"})
    for link in html_soup.findAll('div', {"class": "card no-rationale square-cover apps small"}):
        href = link.a.get("href")
        apps_urls.add("https://play.google.com" + href)

    for app_url in apps_urls:

        driver.implicitly_wait(30)
        time.sleep(2)
        driver.get(app_url + "&showAllReviews=true")
        try:
            new_soup = BeautifulSoup(driver.page_source, 'lxml')
        except:
            continue
        app_title = (new_soup.find('h1', {"class": "AHFaub"})).text
        appsList.append(app_title)
        span = new_soup.findAll('span', jsname="bN97Pc")
        reviews = []
        for s in span:
            reviews.append(s.text)
        appsDict[app_title] = reviews

    driver.close()
    with open('reviews.txt', 'w') as outfile:
        json.dump(appsDict, outfile)


if __name__ == "__main__":
    appsDict = {}
    appsList = list()
    getReviews(appsDict, appsList)
