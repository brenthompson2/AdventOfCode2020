# Advent of Code 2020
# Brendan Thompson
# Day 04
# Star 1
# 
# 
# WARNING: THIS GIVES THE INCORRECT ANSWER
# This is saying there are 180 valid passports while the answer is 179. One passport is slipping through.
# 
# When I submitted the correct answer I actually had an error that was accidentally blocking 2 extra passports,
# as well as an error parsing my test data that was accidentally blocking 1 extra passport but not with the real data.
# So when I ran it on real data, with a bug blocking 2 passports (178 valid), while expecting a different bug causing 1 blocked passport (so actually 179 valid), I ended up with the right answer

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
        # print("\tParsing line:", i, line)
        credential.update(data)

        i = i + 1
        if i == len(lines):
            break

        line = lines[i]
        data = parse_line(line)

    i = i + 1
    # print(credential)
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
        if index_next_whitespace == -1 and '\n' not in line:
            value = line[index+4:]
        else:
            value = line[index+4:index_next_whitespace]
        index = index + len(key) + 1 + len(value) + 1
        # print(key, value)
        data[key] = value
        key = line[index:index+3]
    
    return data

def is_valid_credential(credential):
    """Get whether or not all of the required data is in the credential"""
    if len(credential) < 7:
        print("Expected at least 7 fields, not", len(credential))
        return False
    if len(credential) == 7 and "cid" in credential:
        print("Expected at least 7 fields not including the cid")
        return False

    # Validate byr
    byr = credential["byr"]
    if len(byr) != 4:
        print("Expected byr to be 4 digits, not", len(byr))
        return False
    if not byr.isdigit():
        print("Expected byr to be a number, not", byr)
        return False   
    if int(byr) not in range(1920, 2003):
        print("Invalid byr", byr)
        return False

    # Validate iyr
    iyr = credential["iyr"]
    if len(iyr) != 4:
        print("Expected iyr to be 4 digits, not", len(iyr))
        return False
    if not iyr.isdigit():
        print("Expected iyr to be a number, not", iyr)
        return False   
    if int(iyr) not in range(2010, 2021):
        print("Invalid iyr", iyr)
        return False

    # Validate eyr
    eyr = credential["eyr"]
    if len(eyr) != 4:
        print("Expected eyr to be 4 digits, not", len(eyr))
        return False
    if not eyr.isdigit():
        print("Expected eyr to be a number, not", eyr)
        return False   
    if int(eyr) not in range(2020, 2031):
        print("Invalid eyr", eyr)
        return False

    # Validate hgt
    hgt = credential["hgt"]
    unit = hgt[-2:]
    value = hgt[:-2]
    if unit == "cm":
        if int(value) not in range(150, 194):
            print("Invalid hgt in cm", value)
            return False
    if unit == "in" and int(value) not in range(59, 77):
        print("Invalid hgt in in", value)
        return False

    # Validate hcl
    hcl = credential["hcl"]
    valid_hex = ["a", "b", "c", "d", "e", "f", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    if len(hcl) != 7:
        print("Expected hcl to be 7 characters, not", len(hcl), hcl)
        return False
    for c in hcl[1:]:
        if c not in valid_hex:
            print("Invalid hex value", c)
            return False

    # Validate ecl
    ecl = credential["ecl"]
    valid_ecls = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    if ecl not in valid_ecls:
        print("Unknown ecl", ecl)
        return False

    # Validate pid
    pid = credential["pid"]
    if len(pid) != 9:
        print("Expected pid to be 9 characters, not", len(pid), pid)
        return False   
    if not pid.isdigit():
        print("Expected pid to be a number, not", pid)
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
    # print("\nParsing line", i)
    # print("Num Valid Credentials:", len(credentials))
    # print("Num Invalid Credentials:", num_invalid_credentials)
    (credential, i) = parse_next_entry(lines, i)
    # print("Parsed Credential:", credential)
    if credential == INVALID_CREDENTIAL:
        num_invalid_credentials = num_invalid_credentials + 1
    else:
        credentials.append(credential)

# Return
print("Num Valid Credentials:", len(credentials))
print("Num Invalid Credentials:", num_invalid_credentials)