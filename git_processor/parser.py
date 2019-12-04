import os


def __format_values(line):
    try:
        value = line.strip().split('\t')
        return [value[1], int(value[0])]
    except IndexError:
        return line


def split_in_list(project):
    return [__format_values(line) for line in project.split('\n')][1:]


def extract_raw(project_string):
    if os.path.exists(os.path.dirname(project_string)):
        project_string = read(project_string)

    return [line.strip() for line in project_string.strip().split('\n\n')]


def read(filename):
    with open(filename) as f:
        return f.read()
