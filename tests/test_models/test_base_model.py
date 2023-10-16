#!/usr/bin/python3
"""test_base_model module for unit testing BaseModel Class"""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModelClass(unittest.TestCase):
    """Testing BaseModel Class."""

    @classmethod
    def setUpClass(cls):
        cls.case_1 = BaseModel()
        cls.case_2 = BaseModel()
        cls.case_3 = BaseModel()

    @classmethod
    def tearDownClass(cls):
        pass

    def test_attr_types(self):
        """Testing BaseModel instance attributes types."""
        self.assertIsInstance(self.case_1.id, str)
        self.assertIsInstance(self.case_1.created_at, datetime)
        self.assertIsInstance(self.case_1.updated_at, datetime)

    def test_values(self):
        """Testing BaseModel instance values."""
        self.assertEqual(self.case_1.created_at, self.case_1.updated_at)
        self.assertNotEqual(self.case_1.id, self.case_2.id)

    def test_str(self):
        """Testing the printed output of BaseModel's Instance."""
        case_1_str = f"[BaseModel] ({self.case_1.id}) ({self.case_1.__dict__})"
        case_2_str = f"[BaseModel] ({self.case_2.id}) ({self.case_2.__dict__})"
        case_3_str = f"[BaseModel] ({self.case_3.id}) ({self.case_3.__dict__})"

        self.assertEqual(self.case_1.__str__(), case_1_str)
        self.assertEqual(self.case_2.__str__(), case_2_str)
        self.assertEqual(self.case_3.__str__(), case_3_str)

    def test_save(self):
        """Testing BaseModel's save method."""
        self.case_3.save()
        self.assertNotEqual(self.case_3.updated_at, self.case_3.created_at)

    def test_to_dict(self):
        """Testing BaseModel's to_dict method."""
        dict_1 = self.case_1.to_dict()
        self.assertIsInstance(dict_1["__class__"], str)
        self.assertEqual(dict_1["__class__"], "BaseModel")
        self.assertIsInstance(dict_1["updated_at"], str)
        self.assertIsInstance(dict_1["created_at"], str)

        dict_2 = self.case_2.to_dict()
        self.assertIsInstance(dict_2["__class__"], str)
        self.assertEqual(dict_2["__class__"], "BaseModel")
        self.assertIsInstance(dict_2["updated_at"], str)
        self.assertIsInstance(dict_2["created_at"], str)


if __name__ == "__main__":
    unittest.main()
