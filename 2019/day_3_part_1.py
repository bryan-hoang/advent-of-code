import re

import util


def main():
    wires = util.read_file('day_3_input.txt', 'str')
    wire_1 = traverse_wire(wires[0])
    wire_2 = traverse_wire(wires[1])
    intersections = wire_1 & wire_2
    closest = min(manhattan_distance(point, (0, 0)) for point in intersections)
    print(closest)


def traverse_wire(wire):
    x = 0
    y = 0
    traversed_points = set()
    for instr in wire.split(','):
        move = re.findall('([LRUD])([0-9]+)', instr)[0]
        direction = move[0]
        steps = int(move[1])
        for _ in range(steps):
            if direction == 'L':
                x -= 1
            elif direction == 'U':
                y += 1
            elif direction == 'R':
                x += 1
            elif direction == 'D':
                y -= 1
            traversed_points.add((x, y))
    return traversed_points


def manhattan_distance(point_1, point_2):
    return abs(point_1[0] - point_2[0]) + abs(point_1[1] - point_2[1])


if __name__ == '__main__':
    main()
