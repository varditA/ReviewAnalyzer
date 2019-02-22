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

    # todo more reviews per game?
    reviews_num = len(text)
    # print("reviews num: ", reviews_num)
    if reviews_num < 40:
        return

    # print("function get_most_popular_trigrams")
    # n_gram_results = infoExtraction.get_most_popular_trigrams(text, 3)
    # print(n_gram_results)
    # neg_sents = sentimentAnalyzer.analyzerFunc(n_gram_results)
    # print(neg_sents)
    # results_analyzer.plot_reviews_analysis(appName, n_gram_results, topics, "files/games/")

    # print("function get_sentences_most_popular_trigrams")
    # get all the trigrams from the reviews
    n_gram_results = info_extraction.get_sentences_most_popular_trigrams(text, 3)
    # print(n_gram_results)
    # analyze the sentiment of each trigram, find only the negative trigrams
    neg_sents = sentiment_analyzer.analyzerFunc(n_gram_results)
    # print(neg_sents)
    # plot the neg trigrams by the topic
    results_analyzer.plot_reviews_analysis(app_name, n_gram_results, topics, "Graphs/")


def info_all_apps(app_names, popular_topics):
    for app_name in app_names:
        print(app_name)
        get_app_negative_reviews(app_name, popular_topics)


def main():

    with open('files/info_manual.txt') as json_file:
        data = json.load(json_file)
        app_names = data["app_names"]
        popular_topics = data["popular_topics"]

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
