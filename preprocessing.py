import json

# crawling google play to extract the reviews for each app
import crawler

# getting the popular subjects
import topicExtractor

topic_num = 10


def main():
    projects = {}
    app_names = []
    crawler.getReviews(projects, app_names)
    popular_subjects = topicExtractor.get_apps_popular_nn_aj(projects, topic_num)

    # projects["a"] = "b"
    # projects["c"] = "d"
    # popular_subjects = ["aaa", "bbb", "ccc"]
    # app_names = ["a", "c"]

    data = {"app_names": app_names, "popular_subjects": popular_subjects}
    with open('info.txt', 'w') as outfile:
        json.dump(data, outfile)


if __name__ == "__main__":
    main()
