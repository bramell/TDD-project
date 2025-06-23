import unittest
import text_tool

'''
This is a simple project for practicing Test-Driven Development (TDD) with Python.
The tests were written first e.g test_word_count was written with the intention to fail and no other test was written at that point. 
The intention is to assert that the test actually fails to know that the test is working correctly.

---------------------------------------------------
Start code:

    # Running this function will raise an AttributeError because the add function does not exist yet.
    def test_word_count(self):
        self.assertEqual(text_tool.word_count("Hello World"), 2)

    if __name__ == '__main__':
    unittest.main()
---------------------------------------------------

1. Run the test file to see the test fail. (python3 -m unittest test_text_tool.py)
2. Write the minimum amount of code to make the test pass.
3. Run the test file again to see the test pass. Refactor the code if necessary.
4. Write more tests to cover other functionalities.
'''

class TestTextTool(unittest.TestCase):
    def test_word_count(self):
        self.assertEqual(text_tool.word_count("Hello world"), 2)
        self.assertEqual(text_tool.word_count("He is dumb"), 3)



if __name__ == '__main__':
    unittest.main()