def main():
    with open('./day_6_input.txt') as file:
        memory_banks = [int(memory_bank.strip()) for memory_bank in file.read().split()]
    cycle_count = reallocate(memory_banks)
    print('{} redistribution cycles must be completed.'.format(cycle_count))


def reallocate(memory_banks: list) -> int:
    number_of_cycles = 0
    seen_configurations = [memory_banks.copy()]
    have_seen_same_config = False
    while not have_seen_same_config:
        redistribute_cycle(memory_banks)
        number_of_cycles += 1
        for config in seen_configurations:
            if memory_banks == config:
                have_seen_same_config = True
        seen_configurations.append(memory_banks.copy())
    return number_of_cycles


def redistribute_cycle(memory_banks: list):
    chosen_memory_bank = memory_banks.index(max(memory_banks))
    blocks_to_redistribute = memory_banks[chosen_memory_bank]
    memory_banks[chosen_memory_bank] = 0
    index = chosen_memory_bank
    memory_bank_count = len(memory_banks)
    while blocks_to_redistribute > 0:
        index = (index + 1) % memory_bank_count
        memory_banks[index] += 1
        blocks_to_redistribute -= 1


if __name__ == '__main__':
    main()
