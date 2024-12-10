import unittest
from repositories.reference_repository import create_reference, get_references, delete_reference
from db_helper import delete_table, initialize_database
from config import app

class TestReferenceRepository(unittest.TestCase):
    def setUp(self):
        app.app_context().push()
        delete_table()
        initialize_database()

    def test_create_reference(self):
        create_reference({"author": "test", "title": "test", "journal": "test", "year": "2001", "keyword": "K1234"})
        result = get_references()

        self.assertIsNotNone(result)