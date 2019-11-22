import unittest

from src import name_linter


class NameTest(unittest.TestCase):

    def test_name_with_number(self):
        self.assertTrue(name_linter.compare("owl2", "owl"))
        self.assertFalse(name_linter.compare("owl", "dog"))
        self.assertFalse(name_linter.compare("owl", "dog2"))

        
