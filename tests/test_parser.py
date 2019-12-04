import unittest

from git_processor.data import Projects
from git_processor.parser import read, filter_user
from tests import *


class ParserTest(unittest.TestCase):

    def setUp(self):
        self.p = Projects(TEST_STRING_PROJECTS)

    def test_opendata(self):
        self.assertEqual(TEST_STRING_PROJECTS, read(os.path.join(TEST_PATH, "stats.txt")))

    def test_project_with_path_or_string(self):
        self.assertEqual(str(Projects(os.path.join(TEST_PATH, "stats.txt")).df), str(self.p.df))

    def test_parsed_project(self):
        self.assertEqual(TEST_LIST_PROJECTS, self.p.raw_project_list)
        self.assertEqual(TEST_DICT_PROJECTS, self.p.projects)
        self.assertEqual(TEST_VALUES_PROJECTS, self.p.values_of("project A"))

    def test_parsed_into_dataframe(self):
        self.assertEqual(TEST_DF_PROJECTS, str(self.p.df))

    def test_cleansed_dataframe(self):
        p = Projects(os.path.join(TEST_PATH, "other.txt"))
        self.assertNotEqual(TEST_COMPLEX_CDF_PROJECTS, str(p.df))
        p.clean_up_names()
        self.assertEqual(TEST_COMPLEX_CDF_PROJECTS, str(p.df))

    def test_number_columns(self):
        self.assertEqual(2, self.p.project_number)
        p = Projects(os.path.join(TEST_PATH, "other.txt"))
        self.assertEqual(3, p.project_number)

    def test_filtered(self):
        self.assertEqual(TEST_FILTERED_DF, str(filter_user(self.p.df, ['dog', 'monkey', 'owl'])))
