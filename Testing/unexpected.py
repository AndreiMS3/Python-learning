
import unittest
import math

#Functions given.
def get_sqrt(n):
  return math.sqrt(n)

def divide(a, b):
  return a / b
###

class TestUnexpected (unittest.TestCase):
    #Tests get_sqrt function.
    def test_get_sqrt(self):
        result = math.sqrt(144)
        self.assertEqual(result, 12)
        
    #Checks a negative number is not given.
    def test_negative_input(self):
        with self.assertRaises(ValueError):
            get_sqrt(-5)    #Calls the function to check if the number given is equal or lees than 0.
        
    #Tests divide function. 
    def test_divide(self):
        result = 144/12
        self.assertEqual(result, 12)
        
    #Checks that 0 is not being given as input.
    def test_divided_by_zero(self):
        with self.assertRaises (ZeroDivisionError):
            divide(144,0) #Calls the function to check if the number given is 0.
   
if __name__ == '__main__':
  unittest.main()      
            
