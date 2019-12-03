import unittest

from git_processor.parser import Projects
from tests import *


class DataframeTest(unittest.TestCase):
    
    def setUp(self):
        self.p = Projects(os.path.join(TEST_PATH, "other.txt"))
        self.p.clean_up_names()

    def test_get_total(self):
        self.assertEqual(TEST_TOTAL_PROJECTS, str(self.p.total()))

    def test_get_total_percentage(self):
        self.assertEqual(TEST_PERCENTAGE_PROJECTS, str(self.p.total_percentage()))

    def test_get_percentage_project(self):
        self.assertEqual(TEST_PERCENTAGE_PROJECT, str(self.p.total_project("project B")))

    def test_get_average(self):
        self.assertEqual(TEST_AVERAGE_PROJECT, str(self.p.average()))


if __name__ == "__main__":
    unittest.main()
