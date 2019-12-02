def react_polymer(polymer):
    reaction_occurred = True
    old_length = len(polymer)
    while reaction_occurred:
        for c in "abcdefghijklmnopqrstuvwxyz":
            polymer = polymer.replace(c + c.upper(), "")
            polymer = polymer.replace(c.upper() + c, "")
        reaction_occurred = len(polymer) < old_length
        old_length = len(polymer)
    return polymer


def get_shortest_polymer_length(polymer):
    length_of_different_polymers = []
    for character in "abcdefghijklmnopqrstuvwxyz":
        shortend_polymer = polymer.replace(character, '')
        shortend_polymer = shortend_polymer.replace(character.upper(), '')
        reacted_polymer = react_polymer(shortend_polymer)
        length_of_different_polymers.append(len(reacted_polymer))
    return min(length_of_different_polymers)


def main():
    # :-1 because \n is dumb.
    scanned_polymer = open("./day_5_input.txt").read()[:-1]
    # Part 1
    reacted_polymer = react_polymer(scanned_polymer)
    print(len(reacted_polymer))
    # Part 2
    shortest_polymer_length = get_shortest_polymer_length(scanned_polymer)
    print(shortest_polymer_length)


if __name__ == "__main__":
    main()
