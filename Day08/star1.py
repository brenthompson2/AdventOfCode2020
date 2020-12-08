from utilities import *

# Advent of Code 2020
# Brendan Thompson
# Day 08
# Star 1

def run_script(path):
    """
    Execute the program specified in the data: tracking the accumulator, and printing the accumulator before executing a line twice
    """
    # Read Data
    print("Reading file: ", path, "...")
    data_file = open(path,'r')
    lines = data_file.readlines()
    data_file.close() 

    # Solve
    sum = 0
    i = 0
    lines_visited = []
    while i not in lines_visited:
        lines_visited.append(i)
        (op_code, sign, value) = parse_line(lines[i].strip())

        # Handle Operation
        if op_code == "acc": 
            if sign == "+":
                sum = sum + value
            else:
                sum = sum - value
            i = i + 1
        if op_code == "jmp":
            if sign == "+":
                i = i + value
            else:
                i = i - value
        if op_code == "nop":
            i = i + 1

    # Return
    print("Sum:", sum)

def parse_line(line):
    """
    Get the op_code, sign, and value from the line
    """
    j = 0
    (j, op_code) = get_next_word(j, line)
    j = j + 1
    (j, parameter) = get_next_word(j, line)
    sign = parameter[:1]
    value = int(parameter[1:])
    return (op_code, sign, value)
