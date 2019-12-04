import util


def main():
    instructions = util.read_file('day_2_input.txt', 'str')
    bathroom_code = follow_instructions(instructions)
    print(bathroom_code)


def follow_instructions(instructions: list) -> str:
    keypad = {(0, 2)  : '1',
              (-1, 1) : '2',
              (0, 1)  : '3',
              (1, 1)  : '4',
              (-2, 0) : '5',
              (-1, 0) : '6',
              (0, 0)  : '7',
              (1, 0)  : '8',
              (2, 0)  : '9',
              (-1, -1): 'A',
              (0, -1) : 'B',
              (1, -1) : 'C',
              (0, -2) : 'D'}
    bathroom_code = ''
    x = -2
    y = 0
    for instruction in instructions:
        for move in instruction:
            if move == 'U' and (x, y + 1) in keypad:
                y += 1
            elif move == 'R' and (x + 1, y) in keypad:
                x += 1
            elif move == 'D' and (x, y - 1) in keypad:
                y -= 1
            elif move == 'L' and (x - 1, y) in keypad:
                x -= 1
        bathroom_code += keypad[(x, y)]
    return bathroom_code
    pass


if __name__ == '__main__':
    main()
