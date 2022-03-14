import unittest
import main
from methodFile import DevTools as DT


class TestFunctions(unittest.TestCase):

    def TestCity(self):
        self.assertEqual(type(main.city), str, True)
    def TestLatt(self):
        self.assertEqual(type(main.lattitude) , float , True)
    def TestLong(self):
        self.assertEqual(type(main.longitude), float, True)
