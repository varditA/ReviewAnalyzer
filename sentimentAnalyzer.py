import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer


def get_sentiment(sid, sentence):
    ss = sid.polarity_scores(sentence)
    sentiment = max(ss, key=ss.get)
    return sentiment, ss[sentiment]


def zip_similar_sents(n_gram_results):
    dict_by_word = {}
    for (res, sent, prob) in n_gram_results:
        tagger = nltk.pos_tag(res)
        for (word, tag) in tagger:
            if 'NN' in tag:
                if word in dict_by_word:
                    dict_by_word[word].append((sent, prob))
                else:
                    dict_by_word[word] = [(sent, prob)]
    return dict_by_word


def find_neg_sents(dict_by_word):
    neg_sents = []
    for word in dict_by_word:
        max_prob = 0
        max_prob_sent = ""
        neg_counter = 0
        neg_or_pos_counter = 0
        for (sent, prob) in dict_by_word[word]:
            if prob > max_prob:
                max_prob_sent = sent
                max_prob = prob
        neg_sents.append(max_prob_sent)

    return neg_sents


def analyzerFunc(n_gram_results):
    sid = SentimentIntensityAnalyzer()

    result = set()
    for res in n_gram_results:
        sent = ' '.join(res)
        sentiment, prob = get_sentiment(sid, sent)
        if sentiment == 'neg' and prob > 0.6:
            result.add((res, sent, prob))

    dict_by_word = zip_similar_sents(result)
    neg_sents = find_neg_sents(dict_by_word)

    return set(neg_sents)
