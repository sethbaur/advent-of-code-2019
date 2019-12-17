import math

with open('input.txt') as input_file:
    inputs = input_file.readlines()

wire1_moves = inputs[0].replace('\n', '').split(',')
wire2_moves = inputs[1].replace('\n', '').split(',')

def process(moves):
    current = (0, 0)
    points = [current]
    for move in moves:
        op = move[:1]
        dist = int(move[1:])
        if op == 'R':
            for x in range(current[0] + 1, current[0] + dist + 1):
                points.append((x, current[1]))
        if op == 'U':
            for y in range(current[1] + 1, current[1] + dist + 1):
                points.append((current[0], y))
        if op == 'L':
            for x in range(current[0] - 1, current[0] - dist - 1, -1):
                points.append((x, current[1]))
        if op == 'D':
            for y in range(current[1] - 1, current[1] - dist - 1, -1):
                points.append((current[0], y))
        current = points[-1]
    return set(points)

wire1 = process(wire1_moves)
wire2 = process(wire2_moves)

intersections = wire1 & wire2
intersections.remove((0, 0))

calc_distance = lambda point: math.fabs(point[0]) + math.fabs(point[1])
distances = [calc_distance(point) for point in intersections]
print(min(distances))
