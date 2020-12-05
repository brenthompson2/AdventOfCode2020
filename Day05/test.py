import unittest
from star1 import *

# Advent of Code 2020
# Brendan Thompson
# Day 05
# 
# Test Runner

class GetRowTest(unittest.TestCase):
    """
    Class for testing get_row from star1.py
    """
    def test01(self):
        """
        Ensure get_row handles getting the row from the original example
        """
        # Arrange
        id = "FBFBBFFRLR"

        # Act
        result = get_row(id)

        # Assert
        self.assertEqual(44, result)
        
    def test02(self):
        """
        Ensure get_row handles getting the row from the first other example
        """
        # Arrange
        id = "BFFFBBFRRR"

        # Act
        result = get_row(id)

        # Assert
        self.assertEqual(70, result)
        
    def test03(self):
        """
        Ensure get_row handles getting the row from the second other example
        """
        # Arrange
        id = "FFFBBBFRRR"

        # Act
        result = get_row(id)

        # Assert
        self.assertEqual(14, result)
        
    def test04(self):
        """
        Ensure get_row handles getting the row from the third other example
        """
        # Arrange
        id = "BBFFBBFRLL"

        # Act
        result = get_row(id)

        # Assert
        self.assertEqual(102, result)
 
    def test04_but_ending_with_b(self):
        """
        Ensure get_row handles getting the row from the third other example
        """
        # Arrange
        id = "BBFFBBBRLL"

        # Act
        result = get_row(id)

        # Assert
        # self.assertEqual(103, result)

class GetColumnTest(unittest.TestCase):
    """
    Class for testing get_column from star1.py
    """
    def test01(self):
        """
        Ensure get_column handles getting the column from the original example
        """
        # Arrange
        id = "FBFBBFFRLR"

        # Act
        result = get_column(id)

        # Assert
        self.assertEqual(5, result)
        
    def test02(self):
        """
        Ensure get_column handles getting the column from the first other example
        """
        # Arrange
        id = "BFFFBBFRRR"

        # Act
        result = get_column(id)

        # Assert
        self.assertEqual(7, result)
        
    def test03(self):
        """
        Ensure get_column handles getting the column from the second other example
        """
        # Arrange
        id = "FFFBBBFRRR"

        # Act
        result = get_column(id)

        # Assert
        self.assertEqual(7, result)
        
    def test04(self):
        """
        Ensure get_column handles getting the column from the third other example
        """
        # Arrange
        id = "BBFFBBFRLL"

        # Act
        result = get_column(id)

        # Assert
        self.assertEqual(4, result)
         
class GetSeatIdTest(unittest.TestCase):
    """
    Class for testing get_seat_id from star1.py
    """
    def test01(self):
        """
        Ensure get_seat_id handles getting the seat from the original example
        """
        # Arrange
        id = "FBFBBFFRLR"

        # Act
        result = get_seat_id(id)

        # Assert
        self.assertEqual(357, result)
        
    def test02(self):
        """
        Ensure get_seat_id handles getting the seat from the first other example
        """
        # Arrange
        id = "BFFFBBFRRR"

        # Act
        result = get_seat_id(id)

        # Assert
        self.assertEqual(567, result)
        
    def test03(self):
        """
        Ensure get_seat_id handles getting the seat from the second other example
        """
        # Arrange
        id = "FFFBBBFRRR"

        # Act
        result = get_seat_id(id)

        # Assert
        self.assertEqual(119, result)
        
    def test04(self):
        """
        Ensure get_seat_id handles getting the seat from the third other example
        """
        # Arrange
        id = "BBFFBBFRLL"

        # Act
        result = get_seat_id(id)

        # Assert
        self.assertEqual(820, result)
 
unittest.main()