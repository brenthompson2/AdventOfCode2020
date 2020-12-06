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
    Get the unique characters in a group, while controling the index
    """
    chars = []
    line = lines[i].strip()
    while not is_empty_line(line):
        for char in line:
            chars.append(char)

        i = i + 1
        if i == len(lines):
            break
        line = lines[i].strip()

    i = i + 1
    unique_chars = get_unique(chars)
    return (unique_chars, i)

def is_empty_line(line):
    """
    Get whether or not the line is empty
    https://stackoverflow.com/questions/7896495/python-how-to-check-if-a-line-is-an-empty-line
    """
    return line in ('\n', '\r\n', '')

def get_unique(collection):
    """
    Get the unique items in a collection
    """
    unique = []
    for item in collection:
        if item not in unique:
            unique.append(item)
    return unique