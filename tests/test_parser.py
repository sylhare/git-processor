import unittest

from git_processor.parser import Projects
from tests import *


class ParserTest(unittest.TestCase):

    def setUp(self):
        self.p = Projects(TEST_STRING_PROJECTS)

    def test_opendata(self):
        self.assertEqual(TEST_STRING_PROJECTS, Projects.read(os.path.join(TEST_PATH, "stats.txt")))

    def test_project_with_path_or_string(self):
        self.assertEqual(str(Projects(os.path.join(TEST_PATH, "stats.txt")).df), str(self.p.df))

    def test_parsed_project(self):
        self.assertEqual(TEST_LIST_PROJECTS, self.p.raw_project_list)
        self.assertEqual(TEST_DICT_PROJECTS, self.p.projects)
        self.assertEqual(TEST_VALUES_PROJECTS, self.p.values_of("project A"))

    def test_dataframe(self):
        self.assertEqual(TEST_DF_PROJECTS, str(self.p.df))

    def test_cleansed_dataframe(self):
        p = Projects(os.path.join(TEST_PATH, "other.txt"))
        self.assertNotEqual(TEST_COMPLEX_CDF_PROJECTS, str(p.df))
        p.clean_up_names()
        self.assertEqual(TEST_COMPLEX_CDF_PROJECTS, str(p.df))

    def test_get_total(self):
        p = Projects(os.path.join(TEST_PATH, "other.txt"))
        p.clean_up_names()
        self.assertEqual(TEST_TOTAL_PROJECTS, str(p.total()))
