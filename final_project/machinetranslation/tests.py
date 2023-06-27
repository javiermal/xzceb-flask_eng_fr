import unittest
from translator import french_to_english, english_to_french


class TestModule(unittest.TestCase):
    """only functions that start with "test" will run"""
    def test_englishToFrench(self):
        """Necesseary for Pylint"""
        self.assertEqual(english_to_french("Good Morning"),"Bonjour")
    def test_frenchToEnglish(self):
        """only functions that start with "test" will run"""
        self.assertEqual(french_to_english("Bonjour"),"Hello")
        

if __name__ == '__main__':
    unittest.main()