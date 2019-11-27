import os

import pandas as pd

from src import DATA_PATH
from src.name_linter import *


def open_data(filename="stats.txt", root=DATA_PATH):
    with open(os.path.join(root, filename)) as f:
        return f.read()


class Projects:

    def __init__(self, project_string):
        self.raw_project_list = [line.strip() for line in project_string.strip().split('\n\n')]
        self.projects = {}
        self.setup_project()
        self.__aliases = {}
        self.df = pd.DataFrame(columns=["name"])
        self.setup_dataframe()

    def setup_project(self):
        for project in self.raw_project_list:
            self.projects[project.partition('\n')[0].replace("/", "")] = self.split_in_list(project)

    def values_of(self, project_name):
        return list(zip(*self.projects[project_name]))

    def setup_dataframe(self):
        for key in self.projects:
            df_key = pd.DataFrame(self.projects[key], columns=["name", key])
            self.df = pd.merge(self.df, df_key, on="name", how='outer')
        self.df = self.df.fillna(0)

    def clean_up_names(self):
        self.__create_aliases()
        print(self.__aliases)
        for index, row in self.df.iterrows():
            for key in self.__aliases.keys():
                if row['name'] in self.__aliases[key]:
                    self.df.at[index, 'name'] = key
        self.df = self.__group_by_name()

    @staticmethod
    def format_values(line):
        try:
            value = line.strip().split('\t')
            return [value[1], int(value[0])]
        except IndexError:
            return line

    @staticmethod
    def split_in_list(project):
        return [Projects.format_values(line) for line in project.split('\n')][1:]

    def __create_aliases(self):
        self.df['name'] = self.df['name'].map(lambda x: trim(x))
        self.df = self.__group_by_name()
        self.__aliases = alias_dictionary_of(self.df['name'])

    def __group_by_name(self):
        return self.df.groupby("name").sum().reset_index(level=0)


if __name__ == "__main__":
    data = open_data("test.txt")
    p = Projects(data)
    print(p.df)
    p.clean_up_names()
    print(p.df)
