# crawling google play to extract the reviews for each app
import crawler

# Read the app reviews from the review file
import reviewsExtraction

# Extracts informative phrases from the received reviews
import infoExtraction as info

# Performs sentiment analysis for each of the phrases and remove similar phrases
import sentimentAnalyzer as analyzer


def get_app_negative_reviews(appName):
    # todo
    # text = reviewsExtraction.read_reviews_from_file("reviews.txt", appName)

    # example
    text = reviewsExtraction.read_reviews_from_file("reviews.txt", "https://play.google.com/store/apps/details?id=com.google.android.youtube")

    print(text)
    # text = reviewsExtraction.set_reviews()
    # text = reviewsExtraction.set_reviews2()

    tokens, n_gram_results = info.get_most_popular_trigrams(text, 3)
    print(n_gram_results)
    neg_sents = analyzer.analyzerFunc(n_gram_results)
    print(neg_sents)

    tokens, n_gram_results = info.get_sentences_most_popular_trigrams(text, 3)
    print(n_gram_results)
    neg_sents = analyzer.analyzerFunc(n_gram_results)
    print(neg_sents)


def main():
    # for app in crawler.appList:
    #     results = get_app_negative_reviews(app)
    #     todo save in a file

    # testing
    results = get_app_negative_reviews("")


if __name__ == "__main__":
    main()
