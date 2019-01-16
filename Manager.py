import json

# Read the app reviews from the review file
import reviewsExtraction

# Extracts informative phrases from the received reviews
import infoExtraction as info

# Performs sentiment analysis for each of the phrases and remove similar phrases
import sentimentAnalyzer as analyzer


def get_app_negative_reviews(appName):
    # todo extract reviews from crawling (json file)
    # text = reviewsExtraction.read_reviews_from_file("reviews.txt", appName)
    # todo extract list of popular subjects

    # examples
    text = reviewsExtraction.read_reviews_from_file("reviews.txt", "https://play.google.com/store/apps/details?id=com.google.android.youtube")
    # text = reviewsExtraction.set_reviews()
    # text = reviewsExtraction.set_reviews2()

    print("function get_most_popular_trigrams")
    tokens, n_gram_results = info.get_most_popular_trigrams(text, 3)
    print(n_gram_results)
    neg_sents = analyzer.analyzerFunc(n_gram_results)
    print(neg_sents)

    print("function get_sentences_most_popular_trigrams")
    tokens, n_gram_results = info.get_sentences_most_popular_trigrams(text, 3)
    print(n_gram_results)
    neg_sents = analyzer.analyzerFunc(n_gram_results)
    print(neg_sents)


def main():
    with open('info.txt') as json_file:
        data = json.load(json_file)
        app_names = data["app_names"]
        popular_subjects = data["popular_subjects"]

    # for app in app_names:
        # results = get_app_negative_reviews(app, popular_subjects)
        # todo save in a file

    # testing
    results = get_app_negative_reviews("")


if __name__ == "__main__":
    main()
