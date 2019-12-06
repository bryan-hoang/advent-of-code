import util


def main():
    diagnostic_program = util.read_file('day_5_input.txt', '')
    # test = util.read_file('test_input.txt', '')
    print(diagnostic_program)
    program_output = 0
    memory = diagnostic_program.copy()
    memory[1] = 1
    program_output = run_program(memory)


def run_program(memory: list) -> int:
    current_position = 0
    parameter_modes = list()
    program_input = [1]
    program_output = []
    while True:
        instruction = [digit for digit in str(memory[current_position])]
        current_op_code = instruction[-2:]
        parameter_modes = get_parameter_modes(instruction[-5:-2])
        if current_op_code == 1:
            parameter_1 = get_parameter_value(current_position, memory, parameter_modes[0])
            parameter_2 = get_parameter_value(current_position, memory, parameter_modes[1])
            parameter_3 = get_parameter_value(current_position, memory, parameter_modes[2])
            memory[memory[current_position + 3]] = memory[memory[current_position + 1]] + memory[
                memory[current_position + 2]]
        elif current_op_code == 2:
            memory[memory[current_position + 3]] = memory[memory[current_position + 1]] * memory[
                memory[current_position + 2]]
        elif current_op_code == 3:
            memory[]
        elif current_op_code == 4:
            pass
        current_position += 4

    return memory[0]


def get_parameter_value(current_position, memory, parameter_mode):
    return memory[memory[current_position + 1]] if parameter_mode == 0 else memory[current_position + 1]


def get_parameter_modes(raw_parameter_modes):
    parameter_mode_1, parameter_mode_2, parameter_mode_3 = [0, 0, 0]
    if len(raw_parameter_modes) == 1:
        parameter_mode_1 = raw_parameter_modes[0]
    elif len(raw_parameter_modes) == 2:
        parameter_mode_1 = raw_parameter_modes[1]
        parameter_mode_2 = raw_parameter_modes[0]
    else:
        parameter_mode_1 = raw_parameter_modes[2]
        parameter_mode_2 = raw_parameter_modes[1]
        parameter_mode_3 = raw_parameter_modes[0]
    return parameter_mode_1, parameter_mode_2, parameter_mode_3


if __name__ == '__main__':
    main()
