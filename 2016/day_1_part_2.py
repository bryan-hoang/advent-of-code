import re

import util


def main():
    directions = [[c for c in re.findall('([LR])([0-9]+)', direction)] for direction in
                  util.read_file('day_1_input.txt', '').split(',')]
    print(directions)
    easter_bunny_hq_location = follow_directions(directions)
    print(util.manhattan_distance((easter_bunny_hq_location.real, easter_bunny_hq_location.imag), (0, 0)))


def follow_directions(directions) -> complex:
    current_position = 0
    current_direction = 1
    visited_locations = set()
    visited_locations.add((int(current_position.real), int(current_position.imag)))
    for direction in directions:
        turn, step_count = direction[0]
        current_direction *= 1j if turn == 'L' else -1j
        for _ in range(int(step_count)):
            current_position += current_direction
            if (int(current_position.real), int(current_position.imag)) in visited_locations:
                return current_position
            visited_locations.add((int(current_position.real), int(current_position.imag)))


if __name__ == '__main__':
    main()
