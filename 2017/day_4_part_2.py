from collections import Counter


def main():
    with open('./day_4_input.txt') as file:
        passphrases = [passphrase for passphrase in file.read().split('\n')]
    valid_passphrases_count = get_number_of_valid_passphrases(passphrases)
    print('{} passphrases are valid.'.format(valid_passphrases_count))


def get_number_of_valid_passphrases(passphrases: list) -> int:
    number_of_valid_passphrases = 0
    for passphrase in passphrases:
        number_of_valid_passphrases += is_passphrase_valid(passphrase)
    return number_of_valid_passphrases


def is_passphrase_valid(passphrase: str) -> bool:
    words = passphrase.split()
    for i in range(len(words)):
        for j in range(len(words)):
            if i != j and Counter(words[i]) == Counter(words[j]):
                return False
    return True


if __name__ == '__main__':
    main()
