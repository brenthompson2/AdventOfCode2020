# Advent of Code Day 02
# https://adventofcode.com/2020/day/2

print("Advent of Code Day 02")

def get_min(input):
    index_hyphen = input.index('-')
    return int(input[0:index_hyphen])

def get_max(input):
    index_hyphen = input.index('-')
    index_whitespace = input.index(' ')
    return int(input[index_hyphen + 1:index_whitespace])

def get_character(input):
    index_whitespace = input.index(' ')
    index_colon = input.index(':')
    return input[index_whitespace + 1:index_colon]

def is_valid(min, max, character, input):
    print("min", min,"max", max, "character", character, "input", input)
    count = input.count(character) - 1
    print("count", count)
    result = count in range (min, max + 1)
    print("result", result)
    return result

path = './Day02/data.txt'
print("Reading file: ", path, "...")
data_file = open(path,'r')
items = data_file.readlines()

print("Processing", len(items), "items...")
numValidPasswords = 0
for item in items:
    min = get_min(item)
    max = get_max(item)
    character = get_character(item)
    if is_valid(min, max, character, item):
        numValidPasswords = numValidPasswords + 1
        
data_file.close()
print("Valid passwords:", numValidPasswords)
print("Done")