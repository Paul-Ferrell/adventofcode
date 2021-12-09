from typing import List
from pathlib import Path
import sys

DAYS = 256
CYCLE_LEN = 6
BABY_CYCLE_LEN = 8

def main(input_path: Path):

    fish = parse_data(input_path)

    for day in range(DAYS):
        print("day", day, "num_fish", len(fish))
        multiply(fish)

    print("final_day", day+1,  "num_fish", len(fish))


def parse_data(input_path):

    with input_path.open() as infile:
        return [int(val) for val in infile.readline().strip().split(',')]


def multiply(fish):

    babies = []

    for i in range(len(fish)):

        if fish[i] > 0:
            fish[i] -= 1
        else:
            fish[i] = CYCLE_LEN
            babies.append(BABY_CYCLE_LEN)

    fish.extend(babies)

if __name__ == '__main__':

    if len(sys.argv) > 1:
        input_path = Path(sys.argv[1])
    else:
        input_path = Path('input.txt')

    main(input_path)
