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


def plot_reviews_analysis(app_name, ngrams, topics, file_path):
    """
    Plot the given app reviews analysis results
    :param app_name: The application name
    :param ngrams: list of ngrams
    :param topics: dictionary with topics as keys and list of words os values
    :param file_path: the directory where the file will be saved
    """
    statistics = analyze_results(ngrams, topics)
    total_rating = sum(list(statistics.values())[:-1])
    names = list(statistics.keys())[:-1]
    values = (np.array(list(statistics.values())) / total_rating)[:-1]
    plt.clf()
    plt.title("Reviews breakdown for \"" + app_name + "\"")
    plt.xlabel('Application problems categories')
    plt.ylim(0, 1)
    bar = plt.bar(range(len(values)), values, tick_label=names)

    for col in bar:
        plt.text(col.get_x() + col.get_width() / 2.0,
                 col.get_height(),
                 '{:.2f}'.format(col.get_height()),
                 ha='center',
                 va='bottom')

    name = app_name.replace(" ", "_").replace(":", "-")
    plt.savefig(file_path + name + "_plot.png")
    plt.show()
    print("The graph saved in the 'Graphs' folder with the app name.")


def plot_manual_reviews_analysis(app_name, scores, file_path):
    """
    Plot the given app reviews analysis results
    :param app_name: The application name
    :param scores: list of the scores that the participants gave to each problem according to the application reviews
    :param topics: dictionary with topics as keys and list of words of values
    :param file_path: the directory where the file will be saved
    """
    total_rating = sum([sum(value) for value in scores.values()])
    names = list(scores.keys())
    values = (np.array([sum(value)/len(value) for value in scores.values()]) / (total_rating/3))
    plt.clf()
    plt.title("Manual reviews breakdown for \"" + app_name + "\"")
    plt.xlabel('Application problems categories')
    plt.ylim(0, 1)
    bar = plt.bar(range(len(values)), values, tick_label=names, color='orange')

    for col in bar:
        plt.text(col.get_x() + col.get_width() / 2.0,
                 col.get_height(),
                 '{:.2f}'.format(col.get_height()),
                 ha='center',
                 va='bottom')

    name = app_name.replace(" ", "_").replace(":", "-")
    plt.savefig(file_path + name + "_manual_plot.png")
    plt.show()
    print("The graph saved in the 'Graphs/CompareGraphs' folder with the app name.")

