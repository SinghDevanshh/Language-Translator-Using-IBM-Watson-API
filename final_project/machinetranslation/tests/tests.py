import unittest
from translator import english_to_french, french_to_english


class TestEnglishToFrenchTranslation(unittest.TestCase):
    def test1(self):

        self.assertIsNone(english_to_french(None))
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertNotEqual(english_to_french("Bonjour"),"Hello")

class TestFrenchToEnglishTranslation(unittest.TestCase):
    def test_french_to_english_translation(self):

        self.assertIsNone(english_to_french(None))
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertNotEqual(french_to_english("Hello"),"Bonjour")

unittest.main()
