import json
import os

# crawling google play to extract the reviews for each app
import crawler as crawler

# getting the popular subjects
import tokens_extractor as tokenExtractor

topic_num = 30


def main():
    projects = {}
    app_names = set()

    # crawling Google Play Store
    crawler.getReviews(projects, app_names)

    # getting the popular topics in all the apps
    popular_tokens = tokenExtractor.get_apps_popular_nn_aj(projects, topic_num)

    os.path.abspath('..')

    # updating files' data
    with open('files/reviews.txt', 'w') as outfile:
        json.dump(projects, outfile)

    app_names = list(app_names)
    data = {"app_names": app_names, "tokens_extractor": popular_tokens}
    with open('files/info.txt', 'w') as outfile:
        json.dump(data, outfile)


if __name__ == "__main__":
    main()
