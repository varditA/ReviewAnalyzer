import json

# Read the app reviews from the review file
import reviewsExtraction

# Extracts informative phrases from the received reviews
import infoExtraction

# Performs sentiment analysis for each of the phrases and remove similar phrases
import sentimentAnalyzer

# Plot the apps' reviews analysis results
import results_analyzer


def get_app_negative_reviews(appName):
    # todo extract reviews from crawling (json file)
    text = reviewsExtraction.read_reviews_from_file("reviews.txt", appName)
    # todo extract list of popular subjects

    # examples
    # text = reviewsExtraction.set_reviews()
    # text = reviewsExtraction.set_reviews2()

    # todo fix read data from text
    topics = []
    print("function get_most_popular_trigrams")
    tokens, n_gram_results = infoExtraction.get_most_popular_trigrams(text, 3)
    print(n_gram_results)
    neg_sents = sentimentAnalyzer.analyzerFunc(n_gram_results)
    print(neg_sents)
    results_analyzer.plot_reviews_analysis(appName, n_gram_results, [all])

    print("function get_sentences_most_popular_trigrams")
    tokens, n_gram_results = infoExtraction.get_sentences_most_popular_trigrams(text, 3)
    print(n_gram_results)
    neg_sents = sentimentAnalyzer.analyzerFunc(n_gram_results)
    print(neg_sents)
    results_analyzer.plot_reviews_analysis(appName, n_gram_results, {'all': {'example'}})


def main():
    with open('info.txt') as json_file:
        data = json.load(json_file)
        app_names = data["app_names"]
        popular_subjects = data["popular_subjects"]

    # for app in app_names:
    # results = get_app_negative_reviews(app, popular_subjects)
    # todo save in a file

    # testing
    results = get_app_negative_reviews(app_names[0])


if __name__ == "__main__":
    main()
