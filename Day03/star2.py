# Advent of Code 
# Brendan Thompson
# Day 03
# Star 2
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

def get_num_trees_hit(movement_x, movement_y, map):
    # Get the number of trees ('#') hit given the map and slope
    x = 0
    y = 0
    num_trees_hit = 0
    while (y < len(map)):
        position_contents = map[y][x]
        print("(", x, ",", y, ")")
        print("\t", position_contents)
        if position_contents == '#':
            num_trees_hit = num_trees_hit + 1
            print("\tHit")
        (x, y) = get_next_position(x, y, movement_x, movement_y, map)
    return num_trees_hit

# Read Data
path = './Day03/data.txt'
print("Reading file: ", path, "...")
data_file = open(path,'r')
map = data_file.readlines()
data_file.close()

# Solve
num_trees_slope_1_1 = get_num_trees_hit(1, 1, map)
num_trees_slope_3_1 = get_num_trees_hit(3, 1, map)
num_trees_slope_5_1 = get_num_trees_hit(5, 1, map)
num_trees_slope_7_1 = get_num_trees_hit(7, 1, map)
num_trees_slope_1_2 = get_num_trees_hit(1, 2, map)
product = num_trees_slope_1_1 * num_trees_slope_3_1 * num_trees_slope_5_1 * num_trees_slope_7_1 * num_trees_slope_1_2
print("Product:", product)