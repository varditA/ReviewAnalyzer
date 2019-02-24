import json
# Read the app reviews from the review file
import reviews_extraction
# Extracts informative phrases from the received reviews
import info_extraction

# Performs sentiment analysis for each of the phrases and remove similar phrases
import sentiment_analyzer

# Plot the apps' reviews analysis results
import results_analyzer


def get_app_negative_reviews(app_name, topics):
    # extract reviews from the file the crawler created
    text = reviews_extraction.read_reviews_from_file("files/reviews.txt", app_name)

    reviews_num = len(text)
    if reviews_num < 100:
        print("The number of reviews is not enough to make assumptions.")
        return

    n_gram_results = info_extraction.get_sentences_most_popular_trigrams(text, 3)
    neg_sents = sentiment_analyzer.analyzerFunc(n_gram_results)
    results_analyzer.plot_reviews_analysis(app_name, n_gram_results, topics, "Graphs/")


def info_all_apps(app_names, popular_topics):
    with open('files/manual_results.txt', 'r') as inputFile:
        human_results = json.load(inputFile)

    for app_name in app_names:
        get_app_negative_reviews(app_name, popular_topics)
        if app_name in human_results:
            results_analyzer.plot_manual_reviews_analysis(app_name, human_results[app_name], "Graphs/CompareResults/")


def main():
    with open('files/info_manual.txt') as json_file:
        data = json.load(json_file)
        popular_topics = data["popular_topics"]

    with open('files/info.txt') as json_file:
        data = json.load(json_file)
        app_names = data["app_names"]

    # run all
    info_all_apps(app_names, popular_topics)

    # User choose which app to run
    # print("Choose an app name from the following list:")
    #
    # index = 1
    # for app_name in app_names[:15]:
    #     print(index, app_name)
    #     index += 1
    #
    # app_num = input('Enter the app num: ')
    # app_name = app_names[int(app_num) - 1]
    # print('You chose the app ' + app_name)
    #
    # get_app_negative_reviews(app_name, popular_topics)


if __name__ == "__main__":
    main()
