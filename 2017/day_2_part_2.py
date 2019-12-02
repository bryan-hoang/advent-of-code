import re


def main():
    with open('./day_2_input.txt') as file:
        spreadsheet = [[int(c) for c in re.findall('([0-9]+)', line)] for line in file.read().split('\n')]
    # print('\n'.join(''.join(str(line)) for line in spreadsheet))
    checksum = compute_checksum(spreadsheet)
    print('The checksum of the spreadsheet is {}!'.format(checksum))


def compute_checksum(spreadsheet: list) -> int:
    sum_of_row_results = 0
    for row in spreadsheet:
        first_number, second_number = find_divisible_numbers(row)
        sum_of_row_results += first_number / second_number
    return sum_of_row_results


def find_divisible_numbers(numbers: list) -> tuple:
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if numbers[i] % numbers[j] == 0 and numbers[i] != numbers[j]:
                return numbers[i], numbers[j]


if __name__ == '__main__':
    main()
