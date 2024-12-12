import unittest
from string_utils import reverse_string,capitalize_string, is_capitalized


class TestStringUtils(unittest.TestCase):
    def test_reverse_string(self):
       result = "ierdnA"
       self.assertEqual(result, reverse_string("Andrei"))
       
    def test_capitalize_string(self):
       result =  "Andrei"
       self.assertEqual(result, capitalize_string("andrei"))
    
    def test_is_capitalized(self):
        self.assertTrue(is_capitalized("Andrei"))

if __name__ == "__main__" :
    unittest.main()   