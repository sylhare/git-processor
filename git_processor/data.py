import pandas as pd

from git_processor.name_linter import *
from git_processor.parser import split_in_list, extract_raw
from git_processor.stats import percentage, average, percentage_total


class Projects:

    def __init__(self, project_string):
        self.raw_project_list = extract_raw(project_string)
        self.projects = {}
        self.__setup_project()
        self.__aliases = {}
        self.df = pd.DataFrame(columns=["name"])
        self.__setup_dataframe()
        self.project_number = len(self.df.set_index('name').columns)

    def values_of(self, project_name):
        return list(zip(*self.projects[project_name]))

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
        return percentage_total(self.total())

    def total_project(self, project):
        return percentage_total(self.df.copy()[['name', project]], project)

    def average_user(self):
        average_user = self.total()
        average_user['average'] = average_user['total'].apply(average(self.project_number))
        return average_user.set_index('name')

    def cross_stats(self):
        project_stats = self.df.copy().set_index('name')
        project_stats['total'] = self.total().set_index('name')['total']
        project_stats['average'] = self.average_user()['average']
        project_stats = project_stats.transpose()
        project_stats['total'] = project_stats.sum(axis=1, skipna=True)
        project_stats['average'] = project_stats['total'].apply(average(len(project_stats.columns)))
        project_stats['total %'] = project_stats['total'].apply(percentage(project_stats['total']['total']))
        return project_stats

    def __setup_project(self):
        for project in self.raw_project_list:
            self.projects[project.partition('\n')[0].replace("/", "")] = split_in_list(project)

    def __setup_dataframe(self):
        for key in self.projects:
            df_key = pd.DataFrame(self.projects[key], columns=["name", key])
            self.df = pd.merge(self.df, df_key, on="name", how='outer')
        self.df = self.df.fillna(0)

    def __create_aliases(self):
        self.df['name'] = self.df['name'].map(lambda x: trim(x))
        self.df = self.__group_by_name()
        self.__aliases = alias_dictionary_of(self.df['name'])

    def __group_by_name(self):
        return self.df.groupby("name").sum().reset_index(level=0)


if __name__ == "__main__":
    import os

    p = Projects(os.path.abspath("other.txt"))
    p.clean_up_names()

    print(p.cross_stats())
