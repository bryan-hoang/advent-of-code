from collections import defaultdict


class Point:
    def __init__(self):
        self.position = 0
        self.values_written = defaultdict(int)
        self.values_written[0] = 1
        self.steps_without_turning = 1
        self.direction = 1
        self.steps_taken = 0
        self.consecutive_steps_taken = 0

    def move(self):
        self.position += self.direction
        self.values_written[self.position] = self.compute_value_currently_written()
        self.steps_taken += 1
        self.consecutive_steps_taken += 1
        if self.consecutive_steps_taken == self.steps_without_turning:
            self.direction *= 1j
            self.consecutive_steps_taken = 0
            self.steps_without_turning += 1 if self.direction == -1 or self.direction == 1 else 0

    def compute_value_currently_written(self) -> int:
        return self.values_written[self.position - self.direction] \
               + self.values_written[self.position + self.direction * 1j] \
               + self.values_written[self.position + self.direction * 1j - self.direction] \
               + self.values_written[self.position + self.direction * 1j + self.direction]


def main():
    with open('day_3_input.txt') as file:
        data = int(file.read())
    point = Point()
    traverse_spiralling_memory_from_point_to_data(point, data)
    print('The first value written that is larger {} is {}'
          .format(data, max(point.values_written.values())))


def traverse_spiralling_memory_from_point_to_data(point: Point, data: int):
    while max(point.values_written.values()) <= data:
        point.move()


if __name__ == '__main__':
    main()
