from utilities import *

# Advent of Code 2020
# Brendan Thompson
# Day 09
# Star 2

def run_script(path, length):
    """
    Execute the program specified in the data: tracking the accumulator, and printing the accumulator before executing a line twice
    """
    # Read Data
    print("Reading file: ", path, "...")
    data_file = open(path,'r')
    lines = data_file.readlines()
    data_file.close()
    lines = [int(x.strip()) for x in lines]

    # Find Invalid Value
    invalid_value = get_invalid_value(lines, length)
    
    # Find Contiguous Range
    i = 0
    while i < len(lines):
        sum = int(lines[i])
        j = i + 1
        while j < len(lines):
            sum = sum + int(lines[j])
            if sum == invalid_value:
                print("Found range", i, "-", j, ":", lines[i:j])
                maximum = max(lines[i:j])
                minimum = min(lines[i:j])
                result = int(maximum) + int(minimum)
                print("Max:", maximum, "Min:", minimum, "Sum:", result)
                return result
            j = j + 1
        i = i + 1

def get_invalid_value(lines, length):
    """
    Get the first number in the list that isn't valid
    """
    i = length
    while i < len(lines):
        if not is_valid(i, lines, length):
            print("Invalid value found at index", i, ":", lines[i])
            return int(lines[i])
        i = i + 1

def is_valid(i, lines, length):
    """
    Get whether or not the value at the index is the sum of at least two of the numbers in the previous (length) lines
    """
    value = int(lines[i])
    j = i - length
    while j < i:
        valJ = int(lines[j])
        k = j + 1
        while k < i:
            valK = int(lines[k])
            
            sum = valJ + valK
            if sum == value and valJ != valK:
                return True

            k = k + 1

        j = j + 1

    return False