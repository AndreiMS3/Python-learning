import unittest

def add(a, b):
    return a + b

class TestAddition(unittest.TestCase):
    def test_add(self):
        result = add (3,4)
        
        expect_result = 7
        self.assertEqual(result, expect_result)
        
if __name__ == "__main__":
    unittest.main()        