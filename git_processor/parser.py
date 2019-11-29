import os

import pandas as pd

from git_processor.name_linter import *


class Projects:

    def __init__(self, project_string):
        self.raw_project_list = self.__extract_raw(project_string)
        self.projects = {}
        self.__setup_project()
        self.__aliases = {}
        self.df = pd.DataFrame(columns=["name"])
        self.setup_dataframe()

    def values_of(self, project_name):
        return list(zip(*self.projects[project_name]))

    def setup_dataframe(self):
        for key in self.projects:
            df_key = pd.DataFrame(self.projects[key], columns=["name", key])
            self.df = pd.merge(self.df, df_key, on="name", how='outer')
        self.df = self.df.fillna(0)

    def clean_up_names(self):
        self.__create_aliases()
        for index, row in self.df.iterrows():
            for key in self.__aliases.keys():
                if row['name'] in self.__aliases[key]:
                    self.df.at[index, 'name'] = key
        self.df = self.__group_by_name()

    def total(self):
        total = self.df.set_index('name')
        return total.sum(axis=1, skipna=True).reset_index(name='total')

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

    @staticmethod
    def read(filename):
        with open(filename) as f:
            return f.read()

    def __extract_raw(self, project_string):
        if os.path.exists(os.path.dirname(project_string)):
            project_string = Projects.read(project_string)

        return [line.strip() for line in project_string.strip().split('\n\n')]

    def __setup_project(self):
        for project in self.raw_project_list:
            self.projects[project.partition('\n')[0].replace("/", "")] = self.split_in_list(project)

    def __create_aliases(self):
        self.df['name'] = self.df['name'].map(lambda x: trim(x))
        self.df = self.__group_by_name()
        self.__aliases = alias_dictionary_of(self.df['name'])

    def __group_by_name(self):
        return self.df.groupby("name").sum().reset_index(level=0)
