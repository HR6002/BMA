import unittest
from main import*

class testclass(unittest.TestCase):
    def test_meters(self):
        self.assertEqual(meters(10), 50.292)

