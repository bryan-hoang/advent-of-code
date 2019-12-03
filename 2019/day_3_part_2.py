import re

import util


def main():
    wires = util.read_file('day_3_input.txt', 'str')
    wire_1 = traverse_wire(wires[0])
    wire_2 = traverse_wire(wires[1])
    intersections = set(wire_1) & set(wire_2)
    closest = min(wire_1[point] + wire_2[point] for point in intersections)
    print(closest)


def traverse_wire(wire: str) -> dict:
    x = 0
    y = 0
    jumps = 0
    traversed_points = dict()
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
            jumps += 1
            if (x, y) not in traversed_points:
                traversed_points[(x, y)] = jumps
    return traversed_points


def manhattan_distance(point_1: tuple, point_2: tuple) -> int:
    return abs(point_1[0] - point_2[0]) + abs(point_1[1] - point_2[1])


if __name__ == '__main__':
    main()
