def main():
    with open('./day_6_input.txt') as file:
        memory_banks = [int(memory_bank.strip()) for memory_bank in file.read().split()]
    cycle_count = reallocate(memory_banks)
    print('{} redistribution cycles must be completed.'.format(cycle_count))


def reallocate(memory_banks: list) -> int:
    cycle_count = 0
    seen_configurations = {cycle_count: memory_banks.copy()}
    have_seen_same_config = False
    while True:
        redistribute_cycle(memory_banks)
        cycle_count += 1
        for config in seen_configurations.items():
            if memory_banks == config[1]:
                return cycle_count - config[0]
        seen_configurations[cycle_count] = memory_banks.copy()


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
