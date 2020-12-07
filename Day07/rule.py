from utilities import *

# Advent of Code 2020
# Brendan Thompson
# Day 07
# 
# Data model for a single rule

class Rule():
    """
    The data model for a single rule. Exposes the outer bag color and a dictionary mapping the inner bag colors to the number of them allowed
    """

    def __init__(self, line):
        """Create a new rule given the line of data"""
        # Get outer bag color
        i = 0
        (i, bag_adj) = get_next_word(i, line)
        i = i + 1
        (i, bag_color) = get_next_word(i, line)
        bag = bag_adj + " " + bag_color
        self.outer_bag = bag
        i = i + 1

        # Eat "bags contain"
        (i, _) = get_next_word(i, line)
        i = i + 1
        (i, _) = get_next_word(i, line)
        i = i + 1

        # Check for no bags 
        self.bags = {}
        (i, count) = get_next_word(i, line)
        if count == 'no':
            return

        # Parse bags
        while count != END_OF_LINE:
            i = i + 1
            (i, bag_adj) = get_next_word(i, line)
            i = i + 1
            (i, bag_color) = get_next_word(i, line)
            i = i + 1
            bag = bag_adj + " " + bag_color
            self.bags[bag] = int(count)

            (i, final) = get_next_word(i, line)
            if final[-1] == ".":
                return

            i = i + 1
            (i, count) = get_next_word(i, line)
