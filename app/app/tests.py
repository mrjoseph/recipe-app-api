from django.test import TestCase

from app.calc import add, subtract


class calcTest(TestCase):

    def test_add_numbers(self):
        """Test that 2 numbers are added together"""
        self.assertEqual(add(3, 8), 11)

    def test_subrtract_numbers(self):
        """Test that 2 numbers are subtracted"""
        self.assertEqual(subtract(5, 5), 0)
