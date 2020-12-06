# Advent of Code 2020
# Brendan Thompson
# Day 06
# Star 1

path = './Day06/data.txt'

def run_script():
    """
    Get the number of questions that received a yes response per group
    """
    # Read Data
    print("Reading file: ", path, "...")
    data_file = open(path,'r')
    lines = data_file.readlines()
    data_file.close()

    # Solve
    i = 0
    sum = 0
    while i < len(lines) - 1:
        (unique_chars, i) = parse_batch(lines, i)
        sum = sum + len(unique_chars)

    # Return
    print("Sum:", sum)
        
def parse_batch(lines, i):
    """
    Get the characters mentioned by everyone in the group, while controling the index
    """
    # Create initial collection of chars
    chars = []
    line = lines[i].strip()
    if not is_empty_line(line):
        for char in line:
            chars.append(char)

    # Process remaining collections in group
    i = i + 1
    if i == len(lines):
        return (chars, i)
    line = lines[i].strip()
    while not is_empty_line(line):
        # Trim chars based on line
        updated_chars = []
        for char in chars:
            if char in line:
                updated_chars.append(char)
        chars = updated_chars

        # Get next line
        i = i + 1
        if i == len(lines):
            return (chars, i)
        line = lines[i].strip()

    i = i + 1
    return (chars, i)

def is_empty_line(line):
    """
    Get whether or not the line is empty
    https://stackoverflow.com/questions/7896495/python-how-to-check-if-a-line-is-an-empty-line
    """
    return line in ('\n', '\r\n', '')
