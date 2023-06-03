import unittest
import translator as tr
from translator import french_to_english, english_to_french

class Testt(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english('bonjour'), 'hello')
        self.assertNotEqual(french_to_english('Vie'), 'Hello')


class Test(unittest.TestCase):
    def test2(self):
        self.assertEqual(english_to_french('hello'), 'bonjour')
        self.assertNotEqual(english_to_french('hello'), 'vie')
unittest.main()
