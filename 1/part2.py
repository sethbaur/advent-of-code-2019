import math

def get_sum(mass):
    total = math.floor(int(mass) / 3) - 2
    if total <= 0:
        return 0
    else:
        return total + get_sum(total)


with open('input.txt') as input_file:
    masses = input_file.readlines()

total = 0
for mass in masses:
    total += get_sum(mass)

print(total)
