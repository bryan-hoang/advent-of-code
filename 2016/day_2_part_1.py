import util


def main():
    instructions = util.read_file('day_2_input.txt', 'str')
    bathroom_code = follow_instructions(instructions)
    print(bathroom_code)


def follow_instructions(instructions: list) -> str:
    keypad = {(-1, 1): '1', (0, 1): '2', (1, 1): '3', (-1, 0): '4', (0, 0): '5', (1, 0): '6', (-1, -1): '7',
              (0, -1): '8', (1, -1): '9'}
    bathroom_code = ''
    x = 0
    y = 0
    for instruction in instructions:
        for move in instruction:
            if move == 'U' and y < 1:
                y += 1
            elif move == 'R' and x < 1:
                x += 1
            elif move == 'D' and y > -1:
                y -= 1
            elif move == 'L' and x > -1:
                x -= 1
        bathroom_code += keypad[(x, y)]
    return bathroom_code
    pass


if __name__ == '__main__':
    main()
