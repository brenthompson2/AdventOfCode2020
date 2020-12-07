# Advent of Code 2020
# Brendan Thompson
# 
# A collection of utilities written for Advent of Code 2020

END_OF_LINE = -1

def get_next_word(i, line):
    """
    Get a set containing the updated index and the next word from the line
    """
    if is_empty_line(line[i:]):
        return END_OF_LINE

    word = ""
    while i != len(line) and line[i] != " " and line[i] != "\n":
        word = word + line[i]
        i = i + 1
        
    return (i, word)

def is_empty_line(line):
    """
    Get whether or not the line is empty
    https://stackoverflow.com/questions/7896495/python-how-to-check-if-a-line-is-an-empty-line
    https://stackoverflow.com/questions/2405292/check-if-string-contains-only-whitespace
    """
    return line in ('\n', '\r\n', '') or line.isspace()