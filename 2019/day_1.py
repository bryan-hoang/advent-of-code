module_masses = [int(line) for line in open('day_1_input.txt')]


if __name__ == "__main__":
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
