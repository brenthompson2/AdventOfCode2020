import unittest
from utilities import *
from star1 import parse_line, run_script

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

class ParseLineTest(unittest.TestCase):
    """
    Class for testing parse_line
    """
    def test_parse_line_01_nop(self):
        """
        Ensure parse_line handles parsing nop operations
        """
        # Arrange
        line = "nop +0"

        # Act
        (op_code, sign, value) = parse_line(line)

        # Assert
        self.assertEqual("nop", op_code)
        self.assertEqual("+", sign)
        self.assertEqual(0, value)

    def test_parse_line_02_acm(self):
        """
        Ensure parse_line handles parsing nop operations
        """
        # Arrange
        line = "acm -123"

        # Act
        (op_code, sign, value) = parse_line(line)

        # Assert
        self.assertEqual("acm", op_code)
        self.assertEqual("-", sign)
        self.assertEqual(123, value)

class RunScriptTest(unittest.TestCase):
    """
    Class for testing run_script
    """
    def test_run_script_01_example(self):
        """
        Ensure run_script handles the example
        """
        # Arrange
        path = './Day08/tdata.txt'

        # Act
        sum = run_script(path)

        # Assert
        self.assertEqual(5, sum)

unittest.main()