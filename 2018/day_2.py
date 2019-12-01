def main():
    box_ids = [line for line in open('./input.txt')]

    # Part 1:
    two_letter_id_count = 0
    three_letter_id_count = 0

    for box_id in box_ids:
        two_letter_found = False
        three_letter_found = False
        for letter in 'abcdefghijklmnopqrstuvwxyz':
            if box_id.count(letter) == 2 and not two_letter_found:
                two_letter_id_count += 1
                two_letter_found = True
            if box_id.count(letter) == 3 and not three_letter_found:
                three_letter_id_count += 1
                three_letter_found = True

    checksum = two_letter_id_count * three_letter_id_count

    print('The checksum of the box IDs is %d.' % (checksum))

    # Part 2:

    common_letters = ''

    for first_box_id in box_ids:
        for second_box_id in box_ids:
            character_difference_count = 0
            character_difference_location = -1
            for i in range(len(first_box_id)):
                if first_box_id[i] != second_box_id[i]:
                    character_difference_count += 1
                if character_difference_count == 1 \
                        and first_box_id[i] != second_box_id[i]:
                    character_difference_location = i
            if character_difference_count == 1:
                common_letters = first_box_id \
                    .replace(first_box_id[character_difference_location], '')
                break
        else:
            continue
        break

    print('The common letters of the correct box id are %s'
          % (common_letters))


main()
