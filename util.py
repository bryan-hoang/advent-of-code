from re import findall


def manhattan_distance(point_1: tuple, point_2: tuple) -> int:
    return abs(point_1[0] - point_2[0]) + abs(point_1[1] - point_2[1])


def read_file(file_name, read_mode):
    with open(file_name) as file:
        if read_mode == 'str':
            return [line for line in file]
        elif read_mode == 'int':
            return [int(line) for line in file]
        elif read_mode == 'ints':
            return [int(num) for num in findall('([-+0-9]+)', file.read())]
        else:
            return file.read()


def flat_pack(collection):
    for container in collection:
        for element in container:
            yield element
