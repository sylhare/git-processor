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
        return total.sum(axis=1).reset_index(name='total')

    def user_percentage(self):
        return percentage_total(self.total())

    def user_percentage_project(self, project):
        return percentage_total(self.df.copy()[['name', project]], project)

    def user_average(self):
        average_user = self.total()
        average_user['average'] = average_user['total'].apply(average(self.project_number))
        return average_user.set_index('name')

    def projects_total(self):
        projects = self.df.set_index('name')
        projects['total'] = self.total().set_index('name')['total']
        projects = projects.transpose()
        projects['total'] = projects.sum(axis=1)
        return projects

    def projects_percentage(self):
        projects = self.projects_total()
        projects['total %'] = projects['total'].apply(percentage(projects['total']['total']))
        return projects

    def projects_average(self):
        projects = self.projects_total()
        projects['average'] = projects['total'].apply(average(len(projects.columns)))
        return projects

    def contributors(self):
        return self.df.set_index('name').transpose().astype(bool).sum(axis=1).to_frame(name="contributors")

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

    print(p.user_percentage_project("project C"))
