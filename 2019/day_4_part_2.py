import re

import util


def main():
    test = util.read_file('day_4_input.txt', '')
    lower_bound, upper_bound = re.findall('([0-9]+)-([0-9]+)', test)[0]
    number_of_valid_passwords = count_all_passwords(lower_bound, upper_bound)
    print(number_of_valid_passwords)


def count_all_passwords(lower_bound, upper_bound):
    num_valid_passwords = 0
    for password in range(int(lower_bound), int(upper_bound) + 1):
        num_valid_passwords += does_password_meet_criteria(str(password))
    return num_valid_passwords


def does_password_meet_criteria(password):
    digits = [int(digit) for digit in password]
    is_increasing = digits == sorted(digits)
    consecutive_digits_count = dict()
    for digit in digits:
        consecutive_digits_count[digit] = 0
    for i in range(0, len(digits) - 1):
        if digits[i] == digits[i + 1]:
            consecutive_digits_count[digits[i]] += 1
    contains_digits_repeated_consecutively_once = 1 in consecutive_digits_count.values()
    return is_increasing and contains_digits_repeated_consecutively_once


if __name__ == '__main__':
    main()
