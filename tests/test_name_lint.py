import unittest

from src import name_linter


class NameTest(unittest.TestCase):

    def test_name_with_number(self):
        self.assertTrue(name_linter.compare("owl2", "owl"))
        self.assertFalse(name_linter.compare("owl", "dog"))
        self.assertFalse(name_linter.compare("owl", "dog2"))

    def test_name_with_other_characters(self):
        self.assertTrue(name_linter.compare("owlcoding", "owl.coding"))
        self.assertTrue(name_linter.compare("dôg", "dog"))
        self.assertTrue(name_linter.compare("owlé", "owle"))
        self.assertTrue(name_linter.compare("owlè", "owle"))
        self.assertFalse(name_linter.compare("owl", "dog.dog"))

    def test_name_with_similar_looks(self):
        self.assertTrue(name_linter.compare("The Coding Owl", "owl.coding1"))
        self.assertFalse(name_linter.compare("Super Extra Dog", "Lame Under Dog"))
        self.assertTrue(name_linter.compare("Maté Owly Code", "mowlyco1"))
        self.assertFalse(name_linter.compare("Super Extra Dog", "Maté Owly Code"))
