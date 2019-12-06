import util


def main():
    raw_orbit_map = util.read_file('day_6_input.txt', 'str')
    print(raw_orbit_map)
    orbit_map = construct_orbit_map(raw_orbit_map)
    print(orbit_map)
    orbit_count = count_number_of_orbits(orbit_map)
    print(orbit_count)


def construct_orbit_map(raw_orbit_map):
    orbit_map = dict()
    for orbit in raw_orbit_map:
        objects = orbit.split(')')
        orbit_map[objects[1]] = objects[0]
    return orbit_map


def count_number_of_orbits(orbit_map: dict):
    orbit_count = 0
    for orbit_object in orbit_map.keys():
        while orbit_object in orbit_map.keys():
            orbit_object = orbit_map[orbit_object]
            orbit_count += 1
    return orbit_count


if __name__ == '__main__':
    main()
