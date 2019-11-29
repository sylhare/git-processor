import unittest

from git_processor import name_linter


class NameTest(unittest.TestCase):

    def test_name_with_number(self):
        self.assertTrue(name_linter.is_similar("owl2", "owl"))
        self.assertFalse(name_linter.is_similar("owl", "dog"))
        self.assertFalse(name_linter.is_similar("owl", "dog2"))

    def test_name_with_other_characters(self):
        self.assertTrue(name_linter.is_similar("owlcoding", "owl.coding"))
        self.assertTrue(name_linter.is_similar("dôg", "dog"))
        self.assertTrue(name_linter.is_similar("owlé", "owle"))
        self.assertTrue(name_linter.is_similar("owlè", "owle"))
        self.assertFalse(name_linter.is_similar("owl", "dog.dog"))

    def test_name_with_similar_looks(self):
        self.assertTrue(name_linter.is_similar("The Owl Coding", "owl.coding1"))
        self.assertFalse(name_linter.is_similar("Super Extra Dog", "Lame Under Dog"))
        self.assertTrue(name_linter.is_similar("Maté Owly Code", "mowlyco1"))
        self.assertFalse(name_linter.is_similar("Super Extra Dog", "Maté Owly Code"))
