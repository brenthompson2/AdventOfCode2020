# Advent of Code 2020
# Brendan Thompson
# Day 05
# Star 1

HIGHEST_ROW = 127
HIGHEST_COLUMN = 7
path = './Day05/data.txt'

def run_script():
    """
    Print the highest seat id from all of the bording passes
    """
    # Read Data
    print("Reading file: ", path, "...")
    data_file = open(path,'r')
    lines = data_file.readlines()
    data_file.close()

    # Solve
    highest = 0
    highestValue = 0
    for line in lines:
        id = get_seat_id(line)
        if id > highest:
            highest = id
            highestValue = line

    # Return
    print("Highest:", highest, "-", highestValue)
        
def get_seat_id(line):
    """
    Calculate the id for the seat
    """
    row = get_row(line.strip())
    column = get_column(line.strip())
    return row * 8 + column

def get_row(line):
    """
    Calculate the row id for the seat
    """
    currentLow = 0
    currentHigh = HIGHEST_ROW
    for char in line[:6]:
        half = round(((currentHigh - currentLow) / 2), 0)
        if char == "F":
            currentHigh = currentHigh - half
        else:
            currentLow = currentLow + half
        
    char = line[6]
    if char == "F":
        return currentLow
    else:
        return currentHigh
        
def get_column(line):
    """
    Calculate the column id for the seat
    """
    currentLow = 0
    currentHigh = HIGHEST_COLUMN
    for char in line[7:9]:
        half = round(((currentHigh - currentLow) / 2), 0)
        if char == "L":
            currentHigh = currentHigh - half
        else:
            currentLow = currentLow + half
        
    char = line[9]
    if char == "L":
        return currentLow
    else:
        return currentHigh
