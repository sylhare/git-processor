import unittest

from src.parser import open_data, Projects
from tests import *


class ParserTest(unittest.TestCase):

    def test_opendata(self):
        self.assertEqual(TEST_STRING_PROJECTS, open_data(root=TEST_PATH, filename="test.txt"))

    def test_parsed_project(self):
        p = Projects(TEST_STRING_PROJECTS)
        self.assertEqual(TEST_LIST_PROJECTS, p.raw_project_list)
        self.assertEqual(TEST_DICT_PROJECTS, p.projects)
