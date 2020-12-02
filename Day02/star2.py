# Advent of Code Day 02
# https://adventofcode.com/2020/day/2

print("Advent of Code Day 02")

def get_position_1(input):
    index_hyphen = input.index('-')
    return int(input[0:index_hyphen])

def get_position_2(input):
    index_hyphen = input.index('-')
    index_whitespace = input.index(' ')
    return int(input[index_hyphen + 1:index_whitespace])

def get_character(input):
    index_whitespace = input.index(' ')
    index_colon = input.index(':')
    return input[index_whitespace + 1:index_colon]

def get_password(input):
    index_colon = input.index(':')
    return input[index_colon + 2:]

def is_valid(position_1, position_2, character, password):
    print("position_1", position_1,"position_2", position_2, "character", character, "password", password)
    char_in_position_1 = password[position_1 - 1] == character
    char_in_position_2 = password[position_2 - 1] == character
    if char_in_position_1 == False and char_in_position_2 == False:
        return False
    if char_in_position_1 and char_in_position_2:
        return False
    return True

path = './Day02/data.txt'
print("Reading file: ", path, "...")
data_file = open(path,'r')
items = data_file.readlines()

print("Processing", len(items), "items...")
numValidPasswords = 0
for item in items:
    position_1 = get_position_1(item)
    position_2 = get_position_2(item)
    character = get_character(item)
    password = get_password(item)
    if is_valid(position_1, position_2, character, password):
        numValidPasswords = numValidPasswords + 1
        
data_file.close()
print("Valid passwords:", numValidPasswords)
print("Done")