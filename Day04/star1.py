# Advent of Code 2020
# Brendan Thompson
# Day 04
# Star 1

INVALID_CREDENTIAL = "-1"
END_OF_BATCH = "-2"

def parse_next_entry(lines, i):
    """
    Get the next credential from the next few lines
    Returns INVALID_CREDENTIAL if not all data is found
    """
    credential = {}
    line = lines[i]
    data = parse_line(line)
    while data != END_OF_BATCH:
        print("\tParsing line:", i, line)
        credential.update(data)

        i = i + 1
        if i == len(lines):
            break

        line = lines[i]
        data = parse_line(line)

    i = i + 1
    print(credential)
    if not is_valid_credential(credential):
        return (INVALID_CREDENTIAL, i)
    return (credential, i)

def parse_line(line):
    """
    Get a dictionary of credential data read from the line
    Returns END_OF_BATCH if the line is empty
    """
    if is_empty_line(line):
        return END_OF_BATCH

    index = 0
    key = line[index:index+3]
    data = {}

    while key != "":
        index_next_whitespace = line.find(" ", index)
        value = line[index+4:index_next_whitespace]
        index = index + len(key) + 1 + len(value) + 1
        # print(key, value)
        data[key] = value
        key = line[index:index+3]
    
    return data

def is_valid_credential(credential):
    """Get whether or not all of the required data is in the credential"""
    if len(credential) < 7:
        return False
    if len(credential) == 7:
        if "cid" not in credential:
            return True
        return False
    return True

def is_empty_line(line):
    """
    Get whether or not the line is empty
    https://stackoverflow.com/questions/7896495/python-how-to-check-if-a-line-is-an-empty-line
    """
    return line in ('\n', '\r\n')

# Read Data
path = './Day04/data.txt'
print("Reading file: ", path, "...")
data_file = open(path,'r')
lines = data_file.readlines()
data_file.close()

# Solve
i = 0
num_invalid_credentials = 0
credentials = []
while i < len(lines) - 1:
    print("\nParsing line", i)
    print("Num Invalid Credentials:", num_invalid_credentials)
    (credential, i) = parse_next_entry(lines, i)
    print("Parsed Credential:", credential)
    if credential == INVALID_CREDENTIAL:
        num_invalid_credentials = num_invalid_credentials + 1
    else:
        credentials.append(credential)

# Return
print("Num Valid Credentials:", len(credentials))
print("Num Invalid Credentials:", num_invalid_credentials)