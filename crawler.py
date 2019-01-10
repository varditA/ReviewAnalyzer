from selenium import webdriver
from bs4 import BeautifulSoup
import time

# todo upsate the appList with the apps' names
appsList = list()


def getReviews(projectsDict):
    projects_urls = set()
    url = 'https://play.google.com/store/apps/collection/recommended_for_you?clp=ogoKCAEqAggBUgIIAQ%3D%3D:S:ANO1ljJG6Aw&gsr=Cg2iCgoIASoCCAFSAggB:S:ANO1ljLKNqE'
    # setting up connection, get the info and closing it
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    driver.get(url)

    html_soup = BeautifulSoup(driver.page_source, 'lxml')
    # html_soup.findAll('div', {"class": "card no-rationale square-cover apps small"})
    for link in html_soup.findAll('div', {"class": "card no-rationale square-cover apps small"}):
        href = link.a.get("href")
        projects_urls.add("https://play.google.com" + href)
    for project_url in projects_urls:
        # driver.implicitly_wait(30)
        time.sleep(2)
        driver.get(project_url + "&showAllReviews=true")
        new_soup = BeautifulSoup(driver.page_source, 'html.parser')
        span = new_soup.findAll('span', jsname="bN97Pc")
        reviews = []
        for s in span:
            reviews.append(s.text)
        projectsDict[project_url] = reviews
        # print(reviews)

    driver.close()


if __name__ == "__main__":
    projects = {}
    getReviews(projects)
