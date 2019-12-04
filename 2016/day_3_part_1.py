import util


def main():
    triangles = util.read_file('day_3_input.txt', 'intsperline')
    valid_triangle_count = get_valid_triangle_count(triangles)
    print(valid_triangle_count)


def get_valid_triangle_count(triangles):
    valid_triangle_count = 0
    for triangle in triangles:
        valid_triangle_count += is_valid_triangle(triangle)
    return valid_triangle_count


def is_valid_triangle(triangle):
    return triangle[0] + triangle[1] > triangle[2] \
           and triangle[1] + triangle[2] > triangle[0] \
           and triangle[2] + triangle[0] > triangle[1]


if __name__ == '__main__':
    main()
