def main():
    with open('./day_5_input.txt') as file:
        jumps = [int(line) for line in file]
    current_position = 0
    step_count = 0
    while current_position < len(jumps):
        current_position = take_step(jumps, current_position)
        step_count += 1
    print('It takes {} steps to reach the exit.'.format(step_count))


def take_step(jumps: list, current_position: int) -> int:
    new_position = current_position + jumps[current_position]
    jumps[current_position] += -1 if jumps[current_position] >= 3 else 1
    return new_position


if __name__ == '__main__':
    main()
