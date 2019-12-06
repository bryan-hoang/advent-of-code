def main():
    captcha = open('./day_1_input.txt').read()
    repeated_digits = get_matched_digits(captcha)
    repeated_digits_count = sum(repeated_digits)
    print('The number of repeated digits in the captcha is {}'.format(repeated_digits_count))


def get_matched_digits(captcha: str) -> list:
    repeated_digits = []
    captcha_half_length = len(captcha) // 2
    repeated_captcha = captcha * 2
    for i in range(0, len(captcha)):
        if repeated_captcha[i] == repeated_captcha[i + captcha_half_length]:
            repeated_digits.append(int(repeated_captcha[i]))
    return repeated_digits


if __name__ == '__main__':
    main()
