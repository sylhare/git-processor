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
        self.project_number = len(self.df.set_index('name').columns)

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

    def total_percentage(self):
        return self.__percentage_column('total', self.total())

    def total_project(self, project):
        return self.__percentage_column(project, self.df.copy()[['name', project]])

    def average_user(self):
        average = self.total()
        average['average'] = average['total'].apply(lambda x: int(float(x) / float(self.project_number)))
        return average.set_index('name')

    def cross_stats(self):
        average = self.df.copy().set_index('name')
        average['average'] = self.average_user()['average']
        average['total'] = self.total().set_index('name')['total']
        average = average.transpose()
        average['total'] = average.sum(axis=1, skipna=True)
        average['average'] = average['total'].apply(lambda x: int(float(x) / float(len(average.columns))))
        average['total %'] = average['total'].apply(lambda x: round(100 * float(x) / float(average['total']['total']), 2))
        return average

    @staticmethod
    def __percentage_column(total, column='total'):
        total_commits = total[column].sum()
        total['total %'] = total[column].apply(lambda x: round(100 * float(x) / float(total_commits), 2))
        return total.set_index('name')

    @staticmethod
    def __format_values(line):
        try:
            value = line.strip().split('\t')
            return [value[1], int(value[0])]
        except IndexError:
            return line

    @staticmethod
    def __split_in_list(project):
        return [Projects.__format_values(line) for line in project.split('\n')][1:]

    @staticmethod
    def read(filename):
        with open(filename) as f:
            return f.read()

    @staticmethod
    def __extract_raw(project_string):
        if os.path.exists(os.path.dirname(project_string)):
            project_string = Projects.read(project_string)

        return [line.strip() for line in project_string.strip().split('\n\n')]

    def __setup_project(self):
        for project in self.raw_project_list:
            self.projects[project.partition('\n')[0].replace("/", "")] = self.__split_in_list(project)

    def __create_aliases(self):
        self.df['name'] = self.df['name'].map(lambda x: trim(x))
        self.df = self.__group_by_name()
        self.__aliases = alias_dictionary_of(self.df['name'])

    def __group_by_name(self):
        return self.df.groupby("name").sum().reset_index(level=0)
