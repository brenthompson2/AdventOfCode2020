from rule import *

# Advent of Code 2020
# Brendan Thompson
# Day 07
# Star 2

path = './Day07/data.txt'

def run_script():
    """
    Get the number of bags required for one shiny gold bag
    """
    # Read Data
    rules = parse_rules(path)   

    # Solve
    sum = num_bags_required(rules, "shiny gold")

    # Return
    print("Sum:", sum)

def parse_rules(path_to_rules):
    """
    Get a dictionary of Rules keyed by outer bag color
    """
    # Read Data
    data_file = open(path_to_rules,'r')
    lines = data_file.readlines()
    data_file.close()

    # Parse Rules
    rules = {}
    for line in lines:
        rule = Rule(line)
        rules[rule.outer_bag] = rule  

    return rules

def num_bags_required(rules, color):
    """
    Get the number of bags required by this bag and all of its dependencies
    """
    rule = rules[color]

    if rule.bags == {}:
        return 0
    
    sum = 0
    for bag_color, num_required in rule.bags.items():
        sum = sum + num_required
        sum = sum + (num_required * num_bags_required(rules, bag_color))
    
    return sum