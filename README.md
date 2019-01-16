# ReviewAnalyzer

Files:
_____

preprocessing.py -
Responsible for creating the files with the data needed for the process of the review analyzer.
files: 1. reviews.txt - json format file with the review for each app.
       2. info.txt - includes all the given apps' names and the popular topics in the reviews.

    crawler.py -
    Called by preprocessing.py
    responsible for creating the file with the reviews for each app.

    topicExtractor.py -
    Called by preprocessing.py
    responsible for extracting the most popular nouns and adjectievs in all of the apps' reviews

Manager.py -
Responsible for the whole process of analyzing the negative feedback.
For every app, it analyze its reviews and set its negative feedback in a file

    reviewExtraction.py -
    Called by Manager.py
    For every given app name, it extracts its reviews from a given file

    infoExtraction.py -
    Called by Manager.py
    For every review, it extracts the informative phrases as a bigram/trigram words

    sentimentAnalyzer.py -
    Called by Manager.py
    For every app, it analyzes its phrases and determines its negative feedback

    crawler.py -
    Called by Manager.py
    crawling Google Play Store and write reviews for apps to json file