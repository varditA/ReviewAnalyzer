# ReviewAnalyzer
How to Run:
_________

./run.sh

You will be asked to choose an application and you will receive the algorithm's results for it by a graph. 


Files:
_____

Preprocessing Step:
    preprocessing.py -
    Responsible for creating the files with the data needed for the process of the review analyzer.
    files: 1. reviews.txt - json format file with the review for each app.
           2. info.txt - includes all the given apps' names and the popular tokens in the reviews.

        crawler.py -
        Called by preprocessing.py
        responsible for creating the file with the reviews for each app.

        tokens_extractor.py -
        Called by preprocessing.py
        responsible for extracting the most popular nouns and adjectievs in all of the apps' reviews

Analyzing Step:
    manager.py -
    Responsible for the whole process of analyzing the negative feedback.
    For every app, it analyze its reviews and set its negative feedback in a file.

        review_extraction.py -
        Called by manager.py
        For every chosen app name, it extracts its reviews from a given file.

        info_extraction.py -
        Called by manager.py
        For every review, it extracts the informative phrases as a bigram/trigram words.

        sentiment_analyzer.py -
        Called by manager.py
        For a given app, it analyzes its phrases and determines its negative feedback.

        result_analyzer.py –
        Called by manager.py
        For the given app, plot the analysis results in graph.