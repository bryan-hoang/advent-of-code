frequency = 0

seen_frequencies = set()

current_position = 0

# Note: This is a generator - Alex
file = list(int(line) for line in open('input'))

while True:
    frequency += file[current_position]
    if frequency not in seen_frequencies:
        seen_frequencies.add(frequency)
    else:
        break
    current_position += 1
    if current_position >= len(file):
        current_position = 0

print(frequency)
