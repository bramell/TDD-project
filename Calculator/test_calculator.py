import unittest
import calculator

'''
This is a simple project for practicing Test-Driven Development (TDD) with Python.
The tests were written first e.g test_add was written with the intention to fail and no other test was written at that point. 
The intention is to assert that the test actually fails to know that the test is working correctly.

---------------------------------------------------
Start code:

    # Running this function will raise an AttributeError because the add function does not exist yet.
    def test_add(self):
        self.assertEqual(calculator.add(2, 3), 5)

    if __name__ == '__main__':
    unittest.main()
---------------------------------------------------


TDD workflow below:
1. Run the test file to see the test fail. (python3 -m unittest test_calculator.py)
2. Write the minimum amount of code to make the test pass.
3. Run the test file again to see the test pass. Refactor the code if necessary.
4. Write more tests to cover other functionalities.
'''


class TestCalculator(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(calculator.add(2, 3), 5)
        self.assertEqual(calculator.add(-3, 1), -2)
    
    def test_subtract(self):
        self.assertEqual(calculator.subtract(5, 3), 2)
        self.assertEqual(calculator.subtract(3, 5), -2)
    
    def test_multiply(self):
        self.assertEqual(calculator.multiply(2, 3), 6)
        self.assertEqual(calculator.multiply(-1, 5), -5)
    
    def test_divide(self):
        self.assertEqual(calculator.divide(6, 3), 2)
        self.assertEqual(calculator.divide(5, 2), 2.5)

        # Test if division by zero raises an error, if error is raised the test will pass.
        with self.assertRaises(ValueError):
            calculator.divide(5, 0)


if __name__ == '__main__':
    unittest.main()





'''
        
'''