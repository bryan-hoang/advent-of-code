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
    for direction in directions:
        turn, step_count = direction[0]
        current_direction *= 1j if turn == 'L' else -1j
        current_position += int(step_count) * current_direction
    return current_position


if __name__ == '__main__':
    main()
