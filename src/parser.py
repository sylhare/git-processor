import os

import pandas as pd
import itertools

from src import DATA_PATH
from src.name_linter import trim, is_similar


def open_data(filename="stats.txt", root=DATA_PATH):
    with open(os.path.join(root, filename)) as f:
        return f.read()


class Projects:

    def __init__(self, project_string):
        self.raw_project_list = [line.strip() for line in project_string.strip().split('\n\n')]
        self.projects = {}
        self.setup_project()
        self.df = pd.DataFrame(columns=["name"])
        self.setup_dataframe()

    def setup_project(self):
        for project in self.raw_project_list:
            self.projects[project.partition('\n')[0].replace("/", "")] = self.split_in_list(project)

    def values_of(self, project_name):
        return list(zip(*self.projects[project_name]))

    def setup_dataframe(self):
        for key in self.projects:
            df_key = pd.DataFrame(self.projects[key], columns=[key, "name"])
            self.df = pd.merge(self.df, df_key, on="name", how='outer')
        self.df.fillna(0)

    @staticmethod
    def split_in_list(project):
        return [line.strip().split('\t') for line in project.split('\n')][1:]


def names_and_duplicates(names):
    results = {}
    for a, b in itertools.combinations(names, 2):
        if is_similar(a, b):
            try:
                results[b] += [b]
            except KeyError:
                results[b] = [b]

            if a != b:
                results[b].append(a)
                if is_similar_in(a, results[b]):
                    results.pop(a, None)
    return results


def is_similar_in(a, in_list):
    return len(list(filter(lambda x: is_similar(a, x), in_list))) > 0


if __name__ == "__main__":
    data = open_data("test.txt")
    p = Projects(data)
    p.df['name'] = p.df['name'].map(lambda x: trim(x))
    print(p.df.groupby("name").sum())

    namess = list(p.df['name'])
    result = names_and_duplicates(namess)

    print(result)
