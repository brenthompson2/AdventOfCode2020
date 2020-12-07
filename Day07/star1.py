from rule import *

# Advent of Code 2020
# Brendan Thompson
# Day 07
# Star 1

path = './Day07/data.txt'

def run_script():
    """
    Get the number of bag colors that can eventually contain at least one shiny gold bag
    """
    # Read Data
    rules = parse_rules(path)   

    # Solve
    sum = 0
    for color, rule in rules.items():
        if can_contain_color(rule, rules, "shiny gold", 1):
            sum = sum + 1

    # Return
    print("Sum:", sum)

def parse_rules(path_to_rules):
    """
    Get a dictionary of Rules keyed by outer bag color
    """
    # Read Data
    print("Reading file: ", path_to_rules, "...")
    data_file = open(path_to_rules,'r')
    lines = data_file.readlines()
    data_file.close()

    # Parse Rules
    rules = {}
    for line in lines:
        rule = Rule(line)
        rules[rule.outer_bag] = rule  

    return rules

def can_contain_color(rule, rules, color, count):
    """
    Get whether or not the bag specified in the rule, or any of its subsequent child bags, can contian the specified number of colored bags
    """
    if rule.bags == {}:
        return False
    
    for bag_color, num_allowed in rule.bags.items():
        if bag_color == color and num_allowed >= count:
            return True
        if can_contain_color(rules[bag_color], rules, color, count):
            return True
    
    return False