import unittest
from models.base import Base

class TestBase(unittest.TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0  # Resetting the counter for each test

    def test_auto_id(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id + 1, b2.id)

    def test_specific_id(self):
        b = Base(89)
        self.assertEqual(b.id, 89)

    def test_to_json_string_none(self):
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty_list(self):
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string(self):
        self.assertEqual(Base.to_json_string([{'id': 12}]), '[{"id": 12}]')
        self.assertIsInstance(Base.to_json_string([{'id': 12}]), str)

    def test_from_json_string_none(self):
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty(self):
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json_string(self):
        self.assertEqual(Base.from_json_string('[{"id": 89}]'), [{"id": 89}])
        self.assertIsInstance(Base.from_json_string('[{"id": 89}]'), list)
