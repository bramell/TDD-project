from collections import Counter

'''
This is a simple project for practicing Test-Driven Development (TDD) with Python.
The tests were written first e.g test_add was written with the intention to fail and no other test was written at that point. 
The intention is to assert that the test actually fails to know that the test is working correctly.

---------------------------------------------------
Start code:
    # The minimum amount of code is written to make the test pass.
    def add(a, b):
        return a + b

1. Run the test file to see the test fail. (python3 -m unittest test_calculator.py)
2. Write the minimum amount of code to make the test pass.
3. Run the test file again to see the test pass. Refactor the code if necessary or to optimize.
4. Write more tests to cover other functionalities.
'''

def word_count(text):
    return len(text.split())

def most_common_word(text):
    text.lower()
    # Counter.most_common returns a dict object of counter/word, the (1) returns the most common word and its count and [0][0] refers to only the word.
    return Counter(text.split()).most_common(1)[0][0] 
    