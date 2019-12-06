def main():
    captcha = open('./day_1_input.txt').read()
    immediately_repeated_digits = get_immediately_repeated_digits(captcha)
    immediately_repeated_digits_count = sum(immediately_repeated_digits)
    print('The number of immediately repeated digits in the captcha is {}'.format(immediately_repeated_digits_count))


def get_immediately_repeated_digits(captcha: str) -> list:
    immediately_repeated_digits = []
    for i in range(-1, len(captcha) - 1):
        if captcha[i] == captcha[i + 1]:
            immediately_repeated_digits.append(int(captcha[i]))
    return immediately_repeated_digits


if __name__ == '__main__':
    main()
