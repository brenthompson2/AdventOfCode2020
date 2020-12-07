import unittest
from utilities import *
from rule import *
from star1 import parse_rules, can_contain_color
from star2 import num_bags_required

# Advent of Code 2020
# Brendan Thompson
# Day 07
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

class RuleTest(unittest.TestCase):
    """
    Class for testing the Rule object
    """
    def test_rule_01_no_inner_bags(self):
        """
        Ensure the rule constructor handles there not being any inner bags
        """
        # Arrange
        line = "faded blue bags contain no other bags."

        # Act
        result = Rule(line)

        # Assert
        self.assertEqual("faded blue", result.outer_bag)
        self.assertEqual({}, result.bags)

    def test_rule_02_one_inner_bags(self):
        """
        Ensure the rule constructor handles there being one inner bag
        """
        # Arrange
        line = "bright white bags contain 2 shiny gold bags."

        # Act
        result = Rule(line)

        # Assert
        self.assertEqual("bright white", result.outer_bag)
        self.assertEqual(1, len(result.bags))
        self.assertEqual(2, result.bags["shiny gold"])

    def test_rule_03_multiple_inner_bags(self):
        """
        Ensure the rule constructor handles there being multiple inner bags
        """
        # Arrange
        line = "mirrored gold bags contain 4 mirrored brown bags, 3 dotted coral bags, 4 faded plum bags, 1 mirrored indigo bag."

        # Act
        result = Rule(line)

        # Assert
        self.assertEqual("mirrored gold", result.outer_bag)
        self.assertEqual(4, len(result.bags))
        self.assertEqual(4, result.bags["mirrored brown"])
        self.assertEqual(3, result.bags["dotted coral"])
        self.assertEqual(4, result.bags["faded plum"])
        self.assertEqual(1, result.bags["mirrored indigo"])

class CanContainColorTest(unittest.TestCase):
    """
    Class for testing can_contain_color from star1
    Note that this test expects the example data to be in tdata.txt
    """
    def test_can_contain_color_01_example(self):
        """
        Ensure the algorithm handles the example from the question
        Note that this test expects the example data to be in tdata.txt
        """
        # Arrange
        rules = parse_rules('./Day07/tdata.txt')

        # Act
        a = can_contain_color(rules["bright white"], rules, "shiny gold", 1)
        b = can_contain_color(rules["muted yellow"], rules, "shiny gold", 1)
        c = can_contain_color(rules["dark orange"], rules, "shiny gold", 1)
        d = can_contain_color(rules["light red"], rules, "shiny gold", 1)
        e = can_contain_color(rules["vibrant plum"], rules, "shiny gold", 1)

        # Assert
        self.assertTrue(a)
        self.assertTrue(b)
        self.assertTrue(c)
        self.assertTrue(d)
        self.assertFalse(e)

class NumBagsRequiredTest(unittest.TestCase):
    """
    Class for testing num_bags_required from star2
    Note that this test expects the example data to be in tdata.txt
    """
    def test_num_bags_required_01_example1(self):
        """
        Ensure the algorithm handles the example from the question
        Note that this test expects the example data to be in tdata.txt
        """
        # Arrange
        rules = parse_rules('./Day07/tdata.txt')

        # Act
        a = num_bags_required(rules, "faded blue")
        b = num_bags_required(rules, "dotted black")
        c = num_bags_required(rules, "vibrant plum")
        d = num_bags_required(rules, "dark olive")
        e = num_bags_required(rules, "shiny gold")
        
        # Assert
        self.assertEqual(0, a)
        self.assertEqual(0, b)
        self.assertEqual(11, c)
        self.assertEqual(7, d)
        self.assertEqual(32, e)

unittest.main()