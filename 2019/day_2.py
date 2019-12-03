import util


def main():
    intcode_program = util.read_file('day_2_input.txt', 'ints')

    program_output = 0
    for i in range(100):
        for j in range(100):
            memory = intcode_program.copy()
            memory[1] = i
            memory[2] = j
            program_output = rum_program(memory)
            if program_output == 19690720:
                noun = i
                verb = j
                print(100 * noun + verb)
                break
        else:
            continue
        break


def rum_program(memory: list) -> int:
    current_position = 0
    while True:
        current_opcode = memory[current_position]
        if current_opcode == 1:
            memory[memory[current_position + 3]] = memory[memory[current_position + 1]] + memory[
                memory[current_position + 2]]
        elif current_opcode == 2:
            memory[memory[current_position + 3]] = memory[memory[current_position + 1]] * memory[
                memory[current_position + 2]]
        else:
            break
        current_position += 4

    return memory[0]


if __name__ == "__main__":
    main()
