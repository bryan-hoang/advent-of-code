import re

import util


def main():
    test = util.read_file('day_4_input.txt', '')
    min, max = re.findall('([0-9]+)-([0-9]+)', test)[0]
    number_of_valid_passwords = count_all_passwords(min, max)
    print(number_of_valid_passwords)


def count_all_passwords(min, max):
    num_valid_passwords = 0
    for password in range(int(min), int(max)):
        num_valid_passwords += does_password_meet_criteria(str(password))
    return num_valid_passwords


def does_password_meet_criteria(password):
    digits = [int(digit) for digit in password]
    for i in range(len(password) - 1):
        if digits[i] > digits[i + 1]:
            return False
    return len(digits) != len(set(digits))


if __name__ == '__main__':
    main()
