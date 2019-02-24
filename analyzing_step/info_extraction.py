import string
import nltk
from nltk.corpus import stopwords
from nltk.util import ngrams

nltk.download("stopwords")
nltk.download("punkt")

exclude = set(string.punctuation)
exclude.add("\"")
exclude.add("\"")
stop_words = set(stopwords.words('english'))
stop_words.remove("too")


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

    return trigrams
