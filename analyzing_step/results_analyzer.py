import string
import nltk
from nltk.corpus import stopwords
from nltk.util import ngrams
from collections import Counter

nltk.download("stopwords")
nltk.download("punkt")

exclude = set(string.punctuation)
exclude.add("\"")
exclude.add("\"")
stop_words = set(stopwords.words('english'))
stop_words.remove("too")

# todo delete : old version with top tokens
# def get_most_popular_trigrams(reviews: list, n):
#     concatenated_reviews_with_punctuation = " ".join(r for r in reviews)
#     concatenated_reviews = ''.join(ch for ch in concatenated_reviews_with_punctuation if ch not in exclude)
#     filtered_text = [w for w in concatenated_reviews.split() if w.lower() not in stop_words]
#     concatenated_reviews = ' '.join(w for w in filtered_text)
#     token = nltk.word_tokenize(concatenated_reviews)
#     trigrams = list(ngrams(token, n))
#     tokens = Counter(filtered_text)
#     sorted_tokens = sorted(tokens, key=tokens.get, reverse=True)
#     tagged_tokens = nltk.pos_tag(sorted_tokens)
#     top_tokens = []
#     counter = 0
#     while len(top_tokens) < 5:
#         if "NN" in tagged_tokens[counter][1]:
#             top_tokens.append(sorted_tokens[counter])
#         counter += 1
#     top_tokens = sorted(tokens, key=tokens.get, reverse=True)[:5]
#     top_trigrams = []
#     for trigram in trigrams:
#         if len(set(trigram) & set(top_tokens)) > 0:
#             top_trigrams.append(trigram)
#     return top_tokens, top_trigrams
#
#     # without top tokens
#     return top_tokens, trigrams


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
    # return top_tokens, top_trigrams

    # without top tokens
    return top_tokens, trigrams


def get_most_popular_trigrams(reviews: list, n):
    concatenated_reviews_with_punctuation = " ".join(r for r in reviews)
    concatenated_reviews = ''.join(ch for ch in concatenated_reviews_with_punctuation if ch not in exclude)
    filtered_text = [w for w in concatenated_reviews.split() if w.lower() not in stop_words]
    concatenated_reviews = ' '.join(w for w in filtered_text)
    token = nltk.word_tokenize(concatenated_reviews)
    trigrams = list(ngrams(token, n))

    return trigrams


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
