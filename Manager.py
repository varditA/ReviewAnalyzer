# Scraper for the applications' reviews
import reviewsExtraction

# Extracts informative phrases from the received reviews
import infoExtraction as info

# Performs sentiment analysis for each of the phrases and remove similar phrases
import sentimentAnalyzer as analyzer

def main():
    # text = reviewsExtraction.set_reviews()
    text = reviewsExtraction.set_reviews2()
    tokens, n_gram_results = info.get_most_popular_trigrams(text, 3)

    neg_sents = analyzer.analyzerFunc(n_gram_results)
    print(neg_sents)

if __name__ == "__main__":
    main()
