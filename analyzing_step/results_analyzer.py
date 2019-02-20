import matplotlib.pyplot as plt
import numpy as np


def analyze_results(ngrams, topics):
    """
    :param ngrams: list of ngrams
    :param topics: dictionary with topics as keys and list of words os values
    :return: The percentage of occurrences of each topic in the ngrams
    """
    statistics = dict.fromkeys(topics.keys(), 0)
    statistics['No problem'] = 0
    no_problem_flag = True
    for topic, topic_words in topics.items():
        for w in topic_words:
            for ngram in ngrams:
                if w in ngram:
                    statistics[topic] += 1
                    no_problem_flag = False
            if no_problem_flag:
                statistics['No problem'] += 1
            no_problem_flag = True
    return statistics


def plot_reviews_analysis(app_name, ngrams, topics, file_path="files/games/"):
    """
    Plot the given app reviews analysis results
    :param app_name: The application name
    :param ngrams: list of ngrams
    :param topics: dictionary with topics as keys and list of words os values
    :param file_path: the directory where the file will be saved
    """
    statistics = analyze_results(ngrams, topics)
    total_rating = sum(list(statistics.values()))
    names = list(statistics.keys())
    values = np.array(list(statistics.values())) / total_rating
    plt.clf()
    plt.title("Reviews breakdown for \"" + app_name + "\"")
    plt.xlabel('Application problems categories')
    plt.ylim(0, 1)
    bar = plt.bar(range(len(statistics)), values, tick_label=names)

    for col in bar:
        plt.text(col.get_x() + col.get_width() / 2.0,
                 col.get_height(),
                 '{:.2f}'.format(col.get_height()),
                 ha='center',
                 va='bottom')
    plt.savefig(file_path + app_name.replace(" ", "_") + "_plot.png")
    # plt.show()


# Example that can be deleted
# ngrams_example = [('apple', 'banana', 'orange'), ('pen', 'bike', 'book'), ('dog', 'cat', 'mouse'),
#                   ('apple', 'hello', 'bye'), ('bla', 'apple', 'bla2'), ('bike', 'bla3', 'orange')]
# topics_example = {'fruit': ['apple', 'banana', 'orange', 'kiwi'], 'item': ['pen', 'bike', 'book', 'computer'],
#                   'animal': ['dog', 'cat', 'mouse', 'horse']}
# plot_reviews_analysis("Seven Boom", ngrams_example, topics_example)
