from re import findall


def manhattan_distance(point_1: tuple, point_2: tuple) -> int:
    return abs(point_1[0] - point_2[0]) + abs(point_1[1] - point_2[1])


def read_file(file_name, read_mode: str = 'str'):
    with open(file_name) as file:
        if read_mode == 'str':
            return [line.strip() for line in file]
        elif read_mode == 'int':
            return [int(line) for line in file]
        elif read_mode == 'ints':
            return [int(num) for num in findall('([-+0-9]+)', file.read())]
        elif read_mode == 'intsperline':
            return [[int(num) for num in findall('([-+0-9]+)', line)] for line in file.read().split('\n')]
        else:
            return file.read()


def pack_list(collection: list, grouping_size: int) -> list:
    return [collection[i:i + grouping_size] for i in range(0, len(collection), grouping_size)]


def flat_map(collection):
    for container in collection:
        for element in container:
            yield element
