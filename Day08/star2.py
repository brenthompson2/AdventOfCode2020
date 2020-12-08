from utilities import *

# Advent of Code 2020
# Brendan Thompson
# Day 08
# Star 2

def run_script(path):
    """
    Execute the program specified in the data: tracking the accumulator, and printing the accumulator before executing a line twice
    """
    # Read Data
    lines = load_data(path)

    # Solve
    i = 0
    result = program_terminates(lines)
    while result is False:
        # Get next line with nop or jmp
        i = get_next_nop_or_jmp(i, lines)

        # Swap line
        (op_code, sign, value) = parse_line(lines[i].strip())
        if op_code == "nop":
            updated_line = "jmp" + lines[i][3:]
            lines[i] = updated_line
        else:
            updated_line = "nop" + lines[i][3:]
            lines[i] = updated_line

        # See if program terminates
        result = program_terminates(lines)
        lines = load_data(path)
        i = i + 1


    # Return
    print("Sum:", result)
    return result

def load_data(path):
    """
    Re-read the lines from the file
    """
    data_file = open(path,'r')
    lines = data_file.readlines()
    data_file.close() 
    return lines

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

def get_next_nop_or_jmp(i, lines):
    """
    Get the index of the next "nop" or "jmp" op code
    """
    (op_code, sign, value) = parse_line(lines[i].strip())
    while op_code == "acm" and i < len(i):
        i = i + 1
        (op_code, sign, value) = parse_line(lines[i].strip())
    
    return i

def program_terminates(lines):
    """
    If the specified program terminates return the sum, else return False
    """
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

        if i >= len(lines):
            return sum

    return False