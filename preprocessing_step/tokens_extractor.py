import string
import nltk
from collections import Counter
from nltk.corpus import stopwords

exclude = set(string.punctuation)
exclude.add("“")
exclude.add("”")
stop_words = set(stopwords.words('english'))
stop_words.remove("too")


def process_apps_reviews(apps_reviews):
    text = ""
    for app in apps_reviews.values():
        for review in app:
            text += (" " + review)
    text_without_puct = ''.join(ch for ch in text if ch not in exclude)
    filtered_text = [w for w in text_without_puct.split() if w.lower() not in stop_words]
    concatenated_reviews = ' '.join(w for w in filtered_text)
    tokens = nltk.word_tokenize(concatenated_reviews)
    return tokens


def get_apps_popular_nn_aj(apps_reviews: dict, n):
    """
    Find the most popular nouns and adjectievs in all of the applications reviews
    :param apps_reviews: dictionary of apps names as keys and list of reviews as values
    :param n: the number of words to take
    :return: sorted list of length n of popular nouns and adjectives
    """
    tokens = process_apps_reviews(apps_reviews)
    tagged_tokens = nltk.pos_tag(tokens)
    filtered_tagged_tokens = Counter(
        [tagged_token[0] for tagged_token in tagged_tokens if "NN" in tagged_token[1] or "JJ" in tagged_tokens[1]])
    sorted_tokens = sorted(filtered_tagged_tokens, key=filtered_tagged_tokens.get, reverse=True)
    return sorted_tokens[:n]
