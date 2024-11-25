import unittest
from util import validate_reference, UserInputError


class TestReferenceValidation(unittest.TestCase):
    def setUp(self):
        pass

    def test_valid_author_length_does_not_raise_error(self):
        validate_reference("article", {
                           "author": "test", "title": "test", "journal": "test", "year": "2001", "keyword": "K1234"})

    def test_too_short_or_empty_author_length_raises_error(self):
        with self.assertRaises(ValueError):
            validate_reference(
                "article", {"author": "", "title": "test", "journal": "test", "year": "2001", "keyword": "K1235"})

        with self.assertRaises(ValueError):
            validate_reference(
                "article", {"author": "t", "title": "test", "journal": "test", "year": "2001", "keyword": "K1236"})

    def test_valid_title_length_does_not_raise_error(self):
        validate_reference("article", {
                           "author": "test", "title": "test", "journal": "test", "year": "2001", "keyword": "K1237"})

    def test_too_long_or_short_title_length_raises_error(self):
        with self.assertRaises(ValueError):
            validate_reference(
                "article", {"author": "test", "title": "t", "journal": "test", "year": "2001", "keyword": "K1238"})

        with self.assertRaises(ValueError):
            validate_reference("article", {
                               "author": "test", "title": "test"*100,
                               "journal": "test", "year": "2001", "keyword": "K1239"})
