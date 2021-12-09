from typing import List
from pathlib import Path
import sys

DAYS = 256
CYCLE_LEN = 6
BABY_CYCLE_LEN = 8

def main(input_path: Path):

    fish = parse_data(input_path)

    fish_by_day = {}
    for fishy in fish:
        if fishy in fish_by_day:
            fish_by_day[fishy] += 1
        else:
            fish_by_day[fishy] = 1

    for day in range(DAYS):
        print('day', day, 'num_fish', sum(fish_by_day.values()))
        fish_by_day = multiply(fish_by_day)

    print('final_day', day+1, 'num_fish', sum(fish_by_day.values()))


def parse_data(input_path):

    with input_path.open() as infile:
        return [int(val) for val in infile.readline().strip().split(',')]


def multiply(fish_by_day):

    new_fish_by_day = {i: 0 for i in range(9)}

    for day, count in fish_by_day.items():
        if day != 0:
            new_fish_by_day[day - 1] += count
        else:
            new_fish_by_day[CYCLE_LEN] += count
            new_fish_by_day[BABY_CYCLE_LEN] = count

    return new_fish_by_day


if __name__ == '__main__':

    if len(sys.argv) > 1:
        input_path = Path(sys.argv[1])
    else:
        input_path = Path('input.txt')

    main(input_path)
