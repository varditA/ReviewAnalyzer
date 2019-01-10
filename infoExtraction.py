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


def get_most_popular_trigrams(reviews: list, n):
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

