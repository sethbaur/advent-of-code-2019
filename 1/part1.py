import math

with open('input.txt') as input_file:
    masses = input_file.readlines()

total = 0
for mass in masses:
    total += math.floor(int(mass) / 3) - 2

print(total)
