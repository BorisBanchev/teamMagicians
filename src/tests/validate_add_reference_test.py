import unittest
from util import validate_reference, UserInputError

class TestReferenceValidation(unittest.TestCase):
    def setUp(self):
        pass

    def test_valid_author_length_does_not_raise_error(self):
        validate_reference("test_author", "test_title", "test_journal",2000)

    def test_too_short_or_empty_author_length_raises_error(self):
        with self.assertRaises(UserInputError):
            validate_reference("","test_title", "test_journal",2000)
        
        with self.assertRaises(UserInputError):
            validate_reference("te","test_title", "test_journal",2000)
    
    def test_valid_title_length_does_not_raise_error(self):
        validate_reference("test_author", "test_title", "test_journal",2000)
    
    def test_too_long_title_length_raises_error(self):
        with self.assertRaises(UserInputError):
            validate_reference("test_author","test_title" * 100, "test_journal",2000)
    
    def test_valid_journal_length_does_not_raise_error(self):
        validate_reference("test_author", "test_title", "test_journal",2000)
    
    def test_too_short_or_empty_journal_length_raises_error(self):
        with self.assertRaises(UserInputError):
            validate_reference("test_author","test_title", "",2000)
        
        with self.assertRaises(UserInputError):
            validate_reference("test_author","test_title", "te",2000)


    def test_valid_year_does_not_raise_error(self):
        validate_reference("test_author", "test_title", "test_journal",2000)
    
    def test_zero_or_too_big_year_raises_error(self):
        with self.assertRaises(UserInputError):
            validate_reference("test_author","test_title", "test_journal",0)
        
        with self.assertRaises(UserInputError):
            validate_reference("test_author","test_title", "test_journal",2026)