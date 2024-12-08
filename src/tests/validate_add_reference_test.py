import unittest
from util import validate_reference, check_valid_keyword, UserInputError

class TestReferenceValidation(unittest.TestCase):
    def setUp(self):
        pass

    def test_valid_author_length_does_not_raise_error(self):
        validate_reference("article", {
                           "author": "test", "title": "test", "journal": "test", "year": "2001", "keyword": "K1234"})

    def test_empty_mandatory_field_raises_error(self):
        with self.assertRaises(ValueError):
            validate_reference(
                "article", {"author": "", "title": "test", "journal": "test", "year": "2001", "keyword": "K1235"})

    def test_too_long_or_short_title_length_raises_error(self):
        with self.assertRaises(ValueError):
            validate_reference(
                "article", {"author": "test", "title": "t", "journal": "test", "year": "2001", "keyword": "K1238"})

        with self.assertRaises(ValueError):
            validate_reference("article", {
                               "author": "test", "title": "test"*1000,
                               "journal": "test", "year": "2001", "keyword": "K1239"})

    def test_used_keyword_raises_error(self):
        with self.assertRaises(ValueError):
            check_valid_keyword("K12222", ["K12222", "K12345", "K123456"])

    def test_valid_keyword_does_not_raise_error(self):
        check_valid_keyword("K12222", ["K12223", "K12345", "K123456"])

    def test_no_optional_fields_maintained_for_misc_raises_error(self):
        with self.assertRaises(ValueError):
            validate_reference(
                "misc", {"author": "", "title": "", "howpublished": "", "month": "", "year": "", "note": "", "keyword": "K1238"})

    def test_one_optional_field_is_maintained_for_misc(self):
            validate_reference(
                "misc", {"author": "Matti Luukkainen", "title": "", "howpublished": "", "month": "", "year": "", "note": "", "keyword": "K1238"})

    def test_no_keyword_raises_error(self):
        with self.assertRaises(ValueError):
            validate_reference("article", {
                               "author": "test", "title": "test",
                               "journal": "test", "year": "2001", "keyword": ""})
    
    def test_invalid_year_raises_error(self):
        with self.assertRaises(ValueError):
            validate_reference(
                "article", {"author": "test", "title": "test", "journal": "test", "year": "-1", "keyword": "K1235"})

        with self.assertRaises(ValueError):
            validate_reference(
                "article", {"author": "test", "title": "test", "journal": "test", "year": "2025", "keyword": "K1236"})
