from collections import defaultdict
from typing import List
from pathlib import Path
import sys

def main(input_path: Path):
    data = get_data(input_path)

    o2 = find_rating(data, mcv)
    co2 = find_rating(data, lcv)

    print('o2', o2)
    print('co2', co2)

    o2 = int(o2, 2)
    co2 = int(co2, 2)

    print('o2', o2)
    print('co2', co2)
    print('answer', o2 * co2)


def get_data(input_path) -> List[str]:
    data = []

    with input_path.open() as input_file:
        for line in input_file:
            if not line:
                continue

            line = line.strip()

            data.append(line)

    return data

def find_rating(values, key_func):
    """Filter items by key_func until only one remains, incrementing the comparison column
    each iteration."""

    values = list(values)
    idx = 0
    while len(values) > 1:
        transposed = list(zip(*values))
        key = list(map(key_func, transposed))

        values = list(filter(lambda value: value[idx] == key[idx], values))
        idx += 1

    return values[0]


def lcv(values: List, default='0'):
    """Return the value in values that occurs least frequently. In case
    of a tie, return the default."""
    
    counts = defaultdict(lambda: 0)

    for value in values:
        counts[value] += 1

    least = None
    least_count = None
    for val, count in counts.items():
        if least_count is None or count < least_count:
            least_count = count
            least = val
        elif least_count == count:
            least = default

    return least


def mcv(values: List, default='1'):
    """As per lcv(), except give the most frequently occuring value."""
    
    counts = defaultdict(lambda: 0)

    for value in values:
        counts[value] += 1

    most = None
    most_count = 0 
    for val, count in counts.items():
        if count > most_count:
            most_count = count
            most = val
        elif count == most_count:
            most = default

    return most


if __name__ == '__main__':

    if len(sys.argv) > 1:
        input_path = Path(sys.argv[1])
    else:
        input_path = Path('input.txt')

    main(input_path)
