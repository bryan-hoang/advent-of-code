def create_map_with_bounding_box(coordinates) -> list:
    min_x_coordinate = min(coordinates, key=lambda coordinate: (coordinate[1][0]))[1][0]
    min_y_coordinate = min(coordinates, key=lambda coordinate: (coordinate[1][1]))[1][1]
    max_y_coordinate = max(coordinates, key=lambda coordinate: (coordinate[1][0]))[1][0]
    max_x_coordinate = max(coordinates, key=lambda coordinate: (coordinate[1][1]))[1][1]
    # print(min_x_coordinate, min_y_coordinate, max_x_coordinate, max_y_coordinate)

    map_width = max_x_coordinate - min_x_coordinate
    map_height = max_y_coordinate - min_y_coordinate

    map_of_points = [['.'] * map_height for _ in range(map_width)]

    for y in range(min_y_coordinate, max_y_coordinate):
        for x in range(min_x_coordinate, max_x_coordinate):
            region = assign_point_to_region((x, y), coordinates)
            map_of_points[x - min_x_coordinate][max_y_coordinate - 1 - y] = region

    return map_of_points


def assign_point_to_region(point: tuple, coordinates: list) -> str:
    distances = dict(
        (given_coordinate[0], manhattan_distance(given_coordinate[1], point)) for given_coordinate in coordinates)
    min_distance = min(distances.values())
    closest_points = [p[0] for p in distances.items() if p[1] == min_distance]
    if len(closest_points) == 1:
        return closest_points[0]
    return '.'


def manhattan_distance(first_point: tuple, second_point: tuple) -> int:
    return abs(first_point[0] - second_point[0]) + abs(first_point[1] - second_point[1])


def find_infinite_regions(map_of_points: list) -> set:
    infinite_regions = set()
    for x in range(len(map_of_points)):
        if map_of_points[x][0] in LABELS:
            infinite_regions.add(map_of_points[x][0])
        if map_of_points[x][-1] in LABELS:
            infinite_regions.add(map_of_points[x][-1])
    for y in range(len(map_of_points[0])):
        if map_of_points[0][y] in LABELS:
            infinite_regions.add(map_of_points[0][y])
        if map_of_points[-1][y] in LABELS:
            infinite_regions.add(map_of_points[-1][y])
    return infinite_regions


def calculate_areas_of_each_region(map_of_points: list, infinite_regions: set) -> dict:
    region_areas = dict((c, 0) for c in LABELS if c not in infinite_regions)
    for region in region_areas.keys():
        region_areas[region] = sum(column.count(region) for column in map_of_points)
    return region_areas


def print_map(map_to_print):
    for y in range(len(map_to_print[0])):
        line = ''
        for x in range(len(map_to_print)):
            line += map_to_print[x][len(map_to_print[0]) - 1 - y] + ' '
        print(line)


def main():
    raw_coordinates = [(int(line.split(',')[0]), int(line.split(',')[1])) for line in open('./day_6_input.txt')]
    coordinates = {}
    coordinate_generator = (coordinate for coordinate in raw_coordinates)
    for c in LABELS:
        coordinates[c] = next(coordinate_generator)
    # print(coordinates)
    # Part 1:
    map_of_points = create_map_with_bounding_box(coordinates.items())
    print_map(map_of_points)
    infinite_regions = find_infinite_regions(map_of_points)
    # print(infinite_regions)
    areas_of_each_region = calculate_areas_of_each_region(map_of_points, infinite_regions)
    print(areas_of_each_region)
    max_area = max(areas_of_each_region.values())
    print(max_area)


LABELS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwx'

if __name__ == "__main__":
    main()
