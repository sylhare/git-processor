import unittest

from src.parser import open_data, Projects
from tests import *


class ParserTest(unittest.TestCase):

    def setUp(self):
        self.p = Projects(TEST_STRING_PROJECTS)

    def test_opendata(self):
        self.assertEqual(TEST_STRING_PROJECTS, open_data(root=TEST_PATH, filename="stats.txt"))

    def test_parsed_project(self):
        self.assertEqual(TEST_LIST_PROJECTS, self.p.raw_project_list)
        self.assertEqual(TEST_DICT_PROJECTS, self.p.projects)
        self.assertEqual(TEST_VALUES_PROJECTS, self.p.values_of("project A"))

    def test_dataframe(self):
        self.assertEqual(TEST_DF_PROJECTS, str(self.p.df))
