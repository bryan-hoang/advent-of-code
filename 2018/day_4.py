import re
from collections import defaultdict


def process_raw_input():
    raw_input = open('day_4_input.txt').readlines()
    guard_schedule = []
    for line in raw_input:
        date_time_info = [*map(int, re.findall(
            '\[([0-9]+)-([0-9]+)-([0-9]+) ([0-9]+):([0-9]+)\]',
            line)[0])]
        parsed_entry = {'year': date_time_info[0],
                        'month': date_time_info[1],
                        'day': date_time_info[2],
                        'hour': date_time_info[3],
                        'minute': date_time_info[4],
                        'event': re.findall('] (.*)', line)[0]}
        guard_schedule.append(parsed_entry)

    guard_schedule.sort(key=lambda e: (e['year'], e['month'], e['day'],
                        e['hour'], e['minute']))
    return guard_schedule


def get_sleepiest_guard(guard_schedule):
    guards_data = defaultdict(lambda: {'sleep time': 0, 'start time': 0, 'unique minutes asleep': [0] * 60})
    guard_on_duty = 0
    for entry in guard_schedule:
        if 'Guard' in entry['event']:
            guard_on_duty = int(re.findall('([0-9]+)', entry['event'])[0])
        elif 'asleep' in entry['event']:
            guards_data[str(guard_on_duty)]['start time'] = entry['minute']
        else:
            guards_data[str(guard_on_duty)]['sleep time'] += entry['minute'] - guards_data[str(guard_on_duty)]['start time']
            for minute in range(guards_data[str(guard_on_duty)]['start time'], entry['minute']):
                guards_data[str(guard_on_duty)]['unique minutes asleep'][minute] += 1
    chosen_guard = max(guards_data.items(), key=lambda e: e[1]['sleep time'])
    # print('\n'.join(map(str, guards_data.items())))
    # print(chosen_guard)
    fav_minute = chosen_guard[1]['unique minutes asleep'].index(max(chosen_guard[1]['unique minutes asleep']))
    return int(chosen_guard[0]), fav_minute


if __name__ == "__main__":
    guard_schedule = process_raw_input()
    # for s in guard_schedule:
    #     print(s)
    sleepiest_guard, fav_minute = get_sleepiest_guard(guard_schedule)
    print(sleepiest_guard, fav_minute, sleepiest_guard * fav_minute)
