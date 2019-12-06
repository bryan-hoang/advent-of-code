import util


def main():
    raw_orbit_map = util.read_file('day_6_input.txt', 'str')
    print(raw_orbit_map)
    orbit_map = construct_orbit_map(raw_orbit_map)
    print(orbit_map)
    orbit_count = count_number_of_orbits(orbit_map)
    print(orbit_count)
    min_val = get_min_transfers_to_santa(orbit_map)
    print(min_val)


def construct_orbit_map(raw_orbit_map):
    orbit_map = dict()
    for orbit in raw_orbit_map:
        left, right = orbit.split(')')
        orbit_map[right] = left
    return orbit_map


def count_number_of_orbits(orbit_map: dict):
    orbit_count = 0
    for orbit_object in orbit_map.keys():
        while orbit_object in orbit_map.keys():
            orbit_object = orbit_map[orbit_object]
            orbit_count += 1
    return orbit_count


def get_min_transfers_to_santa(orbit_map):
    my_path_to_com = list()
    santa_path_to_com = list()
    orbit_object = orbit_map['YOU']
    while orbit_object in orbit_map.keys():
        my_path_to_com.append(orbit_object)
        orbit_object = orbit_map[orbit_object]
    orbit_object = orbit_map['SAN']
    while orbit_object in orbit_map.keys():
        santa_path_to_com.append(orbit_object)
        orbit_object = orbit_map[orbit_object]
    print(my_path_to_com, santa_path_to_com)
    while my_path_to_com[-1] == santa_path_to_com[-1]:
        my_path_to_com.pop()
        santa_path_to_com.pop()
    return len(my_path_to_com) + len(santa_path_to_com)

if __name__ == '__main__':
    main()
