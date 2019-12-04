import unittest

from git_processor.data import Projects
from tests import *


class DataframeTest(unittest.TestCase):

    def setUp(self):
        self.p = Projects(os.path.join(TEST_PATH, "other.txt"))
        self.p.clean_up_names()

    def test_get_total(self):
        self.assertEqual(TEST_TOTAL_PROJECTS, str(self.p.total()))

    def test_get_total_percentage(self):
        self.assertEqual(TEST_PERCENTAGE_USER, str(self.p.user_percentage()))

    def test_get_percentage_project(self):
        self.assertEqual(TEST_PERCENTAGE_USER_PROJECT, str(self.p.user_percentage_project("project B")))

    def test_get_average(self):
        self.assertEqual(TEST_AVERAGE_USER, str(self.p.user_average()))

    def test_get_contributor(self):
        self.assertEqual(TEST_CONTRIBUTORS, str(self.p.contributors()))

    def test_get_project_percentage(self):
        self.assertEqual(TEST_PERCENTAGE_PROJECT, str(self.p.projects_percentage()))

    def test_get_project_average(self):
        self.assertEqual(TEST_AVERAGE_PROJECT, str(self.p.projects_average()))


if __name__ == "__main__":
    unittest.main()
