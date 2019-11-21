import os

from src import ROOT_PATH

TEST_PATH = os.path.join(ROOT_PATH, "tests")

TEST_STRING_PROJECTS = """project A/
   122	hero
   100	dog
    29	owl
     6	loco
     6	monkey
     3	coder
     1	spy

project B/
    12	dog
    10	owl
     5	owl2
     2	coder"""
TEST_LIST_PROJECTS = [
    'project A/\n   122\thero\n   100\tdog\n    29\towl\n     6\tloco\n     6\tmonkey\n     3\tcoder\n     1\tspy',
    'project B/\n    12\tdog\n    10\towl\n     5\towl2\n     2\tcoder']
TEST_DICT_PROJECTS = {
    'project A/': [['122', 'hero'], ['100', 'dog'], ['29', 'owl'], ['6', 'loco'], ['6', 'monkey'], ['3', 'coder'],
                   ['1', 'spy']], 'project B/': [['12', 'dog'], ['10', 'owl'], ['5', 'owl2'], ['2', 'coder']]}
