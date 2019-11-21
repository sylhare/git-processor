import os

from src import DATA_PATH


def open_data(filename):
    with open(os.path.join(DATA_PATH, filename)) as f:
        result = f.read()
        resultlist =
        print(resultlist)
        projects = {}
        for element in resultlist:
            projects[element.partition('\n')[0]] = [line.strip().split('\t') for line in element.split('\n')][1:]
        print(str(projects))
