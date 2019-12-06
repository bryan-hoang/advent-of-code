class Point:
    def __init__(self):
        self.position = 0
        self.steps_without_turning = 1
        self.direction = 1
        self.steps_taken = 0
        self.consecutive_steps_taken = 0

    def move(self):
        self.position += self.direction
        self.steps_taken += 1
        self.consecutive_steps_taken += 1
        if self.consecutive_steps_taken == self.steps_without_turning:
            self.direction *= 1j
            self.consecutive_steps_taken = 0
            self.steps_without_turning += 1 if self.direction == -1 or self.direction == 1 else 0


def main():
    with open('day_3_input.txt') as file:
        data = int(file.read())
    point = Point()
    traverse_spiralling_memory_from_point_to_data(point, data)
    print('The number of steps required to carry the data from the square to the access port is {}'
          .format(abs(point.position.real) + abs(point.position.imag)))


def traverse_spiralling_memory_from_point_to_data(point: Point, data: int):
    for _ in range(point.steps_taken, data - 1):
        point.move()


if __name__ == '__main__':
    main()
