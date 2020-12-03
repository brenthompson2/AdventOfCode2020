# Advent of Code 
# Brendan Thompson
# Day 03
# Star 1
# https://adventofcode.com/2020/day/3

print("Advent of Code Day 03")

def get_next_position(x, y, movement_x, movement_y, map):
    # Get the next position given the current row and height    
    x = x + movement_x
    y = y + movement_y

    # Handle Wrap
    map_width = len(map[0])
    if x >= map_width - 1:
        x = x - map_width + 1
    
    return (x, y)

# Configure
movement_x = 3
movement_y = 1

# Read Data
path = './Day03/data.txt'
print("Reading file: ", path, "...")
data_file = open(path,'r')
map = data_file.readlines()
data_file.close()

# Solve
x = 0
y = 0
num_free_spaces = 0
num_trees_hit = 0
while (y < len(map)):
    position_contents = map[y][x]
    print("(", x, ",", y, ")")
    print("\t", position_contents)
    if position_contents == '#':
        num_trees_hit = num_trees_hit + 1
        print("\tHit")
    else:
        num_free_spaces = num_free_spaces + 1
    (x, y) = get_next_position(x, y, movement_x, movement_y, map)

# Cleanup
print("Num Trees:", num_trees_hit)
print("Num Free Spaces:", num_free_spaces)
print("Done")