import json


def read_reviews_from_file(file_name, app_name):
    with open(file_name) as json_file:
        data = json.load(json_file)
    return data[app_name]
