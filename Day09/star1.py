from utilities import *

# Advent of Code 2020
# Brendan Thompson
# Day 09
# Star 1

def run_script(path, length):
    """
    Execute the program specified in the data: tracking the accumulator, and printing the accumulator before executing a line twice
    """
    # Read Data
    print("Reading file: ", path, "...")
    data_file = open(path,'r')
    lines = data_file.readlines()
    data_file.close() 

    # Solve
    i = length
    while i < len(lines):
        if not is_valid(i, lines, length):
            print(i, "-", lines[i])
            return
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