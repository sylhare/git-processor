import os

from src import DATA_PATH


def open_data(filename="stats.txt", root=DATA_PATH):
    with open(os.path.join(root, filename)) as f:
        return f.read()


class Projects:

    def __init__(self, project_string):
        self.raw_project_list = [line.strip() for line in project_string.strip().split('\n\n')]
        self.projects = {}
        self.setup_project()

    def setup_project(self):
        for project in self.raw_project_list:
            self.projects[project.partition('\n')[0]] = [line.strip().split('\t') for line in project.split('\n')][1:]


if __name__ == "__main__":
    print(open_data("test.txt"))
