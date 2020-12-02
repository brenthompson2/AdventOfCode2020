# Advent of Code Day 01
# https://adventofcode.com/2020/day/1

path = './Day01/data.txt'
print("Reading file: ", path, "...")
data_file = open(path,'r')
items = data_file.readlines()

print("Processing", len(items), "items...")
for i in range(len(items) - 1):
  itemI = int(items[i])
  for j in range(i + 1, len(items)):
    itemJ = int(items[j])
    for k in range(j + 1, len(items)):
      itemK = int(items[k])
      result = itemI + itemJ + itemK
      if result == 2020:
        print(itemI, "+", itemJ, "+", itemK, "=", result)
        product = itemI * itemJ * itemK
        print("Answer = ", product)
        
data_file.close()
print("Done")