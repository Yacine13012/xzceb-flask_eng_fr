import unittest

from translator import french_to_english, english_to_french

class Test_English(unittest.TestCase):
    def test_french_to_english(self):
        self.assertEqual(french_to_english('Bonjour'),'Hello')
        self.assertEqual(french_to_english('Comment'),'How')
        self.assertNotEqual(french_to_english('Vélo'),'Cycle')
        self.assertEqual(french_to_english('Quel âge as-tu?'),'How old are you?')    

class Test_French(unittest.TestCase):
    def test_english_to_french(self):
        self.assertEqual(english_to_french('Hello'),'Bonjour') 
        self.assertEqual(english_to_french('How'),'Comment')  
        self.assertNotEqual(english_to_french('Cycle'),'Vélo')
        self.assertEqual(english_to_french('How old are you?'),'Quel âge as-tu?') 
unittest.main()
