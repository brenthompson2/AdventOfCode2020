import unittest
from utilities import *
from star1 import is_valid
from star2 import run_script

# Advent of Code 2020
# Brendan Thompson
# 
# Test Runner

class UtilitiesTest(unittest.TestCase):
    """
    Class for testing the utilities
    """
    def test_get_next_word_01_no_data(self):
        """
        Ensure get_next_word handles there not being any data
        """
        # Arrange
        line = ""

        # Act
        result = get_next_word(0, line)

        # Assert
        self.assertEqual(END_OF_LINE, result)

    def test_get_next_word_02_whitespace(self):
        """
        Ensure get_next_word handles there just being whitespace
        """
        # Arrange
        line = " "

        # Act
        result = get_next_word(0, line)

        # Assert
        self.assertEqual(END_OF_LINE, result)

    def test_get_next_word_03_empty_line(self):
        """
        Ensure get_next_word handles there just being a newline character
        """
        # Arrange
        line = "\n"

        # Act
        result = get_next_word(0, line)

        # Assert
        self.assertEqual(END_OF_LINE, result)

    def test_get_next_word_04_gets_only_word(self):
        """
        Ensure get_next_word handles there just being a newline character
        """
        # Arrange
        line = "word1"

        # Act
        i = 0
        (i, result1) = get_next_word(i, line)
        result2 = get_next_word(i, line)

        # Assert
        self.assertEqual("word1", result1)
        self.assertEqual(END_OF_LINE, result2)

    def test_get_next_word_05_gets_words(self):
        """
        Ensure get_next_word handles getting multiple words
        """
        # Arrange
        line = "word1 word2 word3 word4"

        # Act
        i = 0
        (i, result1) = get_next_word(i, line)
        i = i + 1
        (i, result2) = get_next_word(i, line)
        i = i + 1
        (i, result3) = get_next_word(i, line)
        i = i + 1
        (i, result4) = get_next_word(i, line)
        i = i + 1
        result5 = get_next_word(i, line)

        # Assert
        self.assertEqual("word1", result1)
        self.assertEqual("word2", result2)
        self.assertEqual("word3", result3)
        self.assertEqual("word4", result4)
        self.assertEqual(END_OF_LINE, result5)

class IsValidTest(unittest.TestCase):
    """
    Class for testing is_valid
    """
    def test_is_valid_01_true(self):
        """
        Ensure is_valid returns true if the value is the sum of at least 2 of the numbers before it
        """
        # Arrange
        lines = [1, 2, 3, 3, 4, 7]

        # Act
        result = is_valid(5, lines, 5)

        # Assert
        self.assertTrue(result)
        
    def test_is_valid_02_duplicate(self):
        """
        Ensure is_valid returns false if the value is
        the sum of at least 2 of the numbers before it, but the same number
        """
        # Arrange
        lines = [1, 2, 3, 3, 1, 6]

        # Act
        result = is_valid(5, lines, 5)

        # Assert
        self.assertFalse(result)

    def test_is_valid_03_false(self):
        """
        Ensure is_valid returns false if the value is not
        the sum of at least 2 of the numbers before it
        """
        # Arrange
        lines = [1, 2, 3, 3, 1, 10]

        # Act
        result = is_valid(5, lines, 5)

        # Assert
        self.assertFalse(result)

class star2Test(unittest.TestCase):
    """
    Class for testing the star2 run_script
    """
    def test_run_script_01_example(self):
        """
        Ensure is_valid returns false if the value is not
        the sum of at least 2 of the numbers before it
        """
        # Arrange
        path = './Day09/tdata.txt'
        length = 5

        # Act
        result = run_script(path, length)

        # Assert
        self.assertEqual(62, result)

       

unittest.main()