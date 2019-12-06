import re


def main():
    with open('./day_2_input.txt') as file:
        spreadsheet = [[int(c) for c in re.findall('([0-9]+)', line)] for line in file.read().split('\n')]
    # print('\n'.join(''.join(str(line)) for line in spreadsheet))
    checksum = compute_checksum(spreadsheet)
    print('The checksum of the spreadsheet is {}!'.format(checksum))


def compute_checksum(spreadsheet: list) -> int:
    sum_of_row_differences = 0
    for row in spreadsheet:
        sum_of_row_differences += max(row) - min(row)
    return sum_of_row_differences


if __name__ == '__main__':
    main()
