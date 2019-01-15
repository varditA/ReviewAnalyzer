import string
import nltk
from nltk.corpus import stopwords
from nltk.util import ngrams
from collections import Counter

exclude = set(string.punctuation)
exclude.add("“")
exclude.add("”")
stop_words = set(stopwords.words('english'))
stop_words.remove("too")

di = {"app1": ["great game, too many ads", "ads all the time in game"], "app2": ["crushes every second, cant play!", "why the app creshes all the??"]}

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
    filtered_tagged_tokens = Counter([tagged_token[0] for tagged_token in tagged_tokens if  "NN" in tagged_token[1] or "JJ" in tagged_tokens[1]])
    sorted_tokens = sorted(filtered_tagged_tokens, key=filtered_tagged_tokens.get, reverse=True)
    print(sorted_tokens[:n])




def get_most_popular_trigrams(reviews: list, n):
    get_apps_popular_nn_aj(di, 100)
    concatenated_reviews_with_punctuation = " ".join(r for r in reviews)
    concatenated_reviews = ''.join(ch for ch in concatenated_reviews_with_punctuation if ch not in exclude)
    filtered_text = [w for w in concatenated_reviews.split() if w.lower() not in stop_words]
    concatenated_reviews = ' '.join(w for w in filtered_text)
    token = nltk.word_tokenize(concatenated_reviews)
    trigrams = list(ngrams(token, n))
    tokens = Counter(filtered_text)
    sorted_tokens = sorted(tokens, key=tokens.get, reverse=True)
    tagged_tokens = nltk.pos_tag(sorted_tokens)
    top_tokens = []
    counter = 0
    while len(top_tokens) < 5:
        if "NN" in tagged_tokens[counter][1]:
            top_tokens.append(sorted_tokens[counter])
        counter += 1
    top_tokens = sorted(tokens, key=tokens.get, reverse=True)[:5]
    top_trigrams = []
    for trigram in trigrams:
        if len(set(trigram) & set(top_tokens)) > 0:
            top_trigrams.append(trigram)
    return top_tokens, top_trigrams


def get_sentences_most_popular_trigrams(reviews: list, n):
    concatenated_reviews_with_punctuation = " ".join(r for r in reviews)
    sentences = concatenated_reviews_with_punctuation.split(".")
    trigrams = []
    tokens = []
    for s in sentences:
        no_punct_sentence = ''.join(ch if ch not in exclude else " " for ch in s)
        filtered_sentence = " ".join(
            word for word in [w for w in no_punct_sentence.split() if w.lower() not in stop_words])
        sentence_tokens = nltk.word_tokenize(filtered_sentence)
        trigrams.extend(list(ngrams(sentence_tokens, n)))
        tokens.extend(sentence_tokens)
    tokens_counter = Counter(tokens)
    sorted_tokens = sorted(tokens_counter, key=tokens_counter.get, reverse=True)
    tagged_tokens = nltk.pos_tag(sorted_tokens)
    top_tokens = []  # only nouns
    counter = 0
    while len(top_tokens) < 5:
        if "NN" in tagged_tokens[counter][1]:
            top_tokens.append(sorted_tokens[counter])
        counter += 1
    top_trigrams = []
    for trigram in trigrams:
        if len(set(trigram) & set(top_tokens)) > 0:
            top_trigrams.append(trigram)
    return top_tokens, top_trigrams
