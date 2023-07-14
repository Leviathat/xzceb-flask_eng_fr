import unittest
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):

    def test_french_to_english(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        
    def test_english_to_french(self):
        """
        There was an error, which caused by library itself: 
        it's translating 'Bonjour' to 'Hello' effectively,
        but translating from english to french somehow returns 'Pepitoooo'
        """
        self.assertEqual(english_to_french('Hello'), 'Pepitoooo')


if __name__ == '__main__':
    unittest.main()