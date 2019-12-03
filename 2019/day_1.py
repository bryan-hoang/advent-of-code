import util


def main():
    module_masses = util.read_file('day_1_input.txt', 'ints')
    # Part 1
    print(sum(((mass // 3 - 2) for mass in module_masses)))

    # Part 2
    total_fuel = 0

    for mass in module_masses:
        fuel = mass // 3 - 2
        while fuel >= 0:
            total_fuel += fuel
            fuel = fuel // 3 - 2

    print(total_fuel)


if __name__ == "__main__":
    main()
