from collections import defaultdict
from typing import List
from pathlib import Path
import sys

def main(input_path: Path):
    data = get_data(input_path)

    transposed = list(zip(*data))

    gamma_rate = ''.join(map(mcv, transposed))
    print('raw_gamma', gamma_rate)
    gamma_rate = int(gamma_rate, 2)

    epsilon_rate = ''.join(map(lcv, transposed))
    print('raw_epsilon', epsilon_rate)
    epsilon_rate = int(epsilon_rate, 2)

    print('gamma_rate', gamma_rate)
    print('epsilon_rate', epsilon_rate)
    print('answer', gamma_rate * epsilon_rate)


def get_data(input_path) -> List[str]:
    data = []

    with input_path.open() as input_file:
        for line in input_file:
            if not line:
                continue

            line = line.strip()

            data.append(line)

    return data


def lcv(values: List):
    """Return the value in values that occurs least frequently. In case
    of a tie, the first occuring value is given."""
    
    counts = defaultdict(lambda: 0)

    for value in values:
        counts[value] += 1

    least = None
    least_count = None
    for val, count in counts.items():
        if least_count is None or count < least_count:
            least_count = count
            least = val

    return least


def mcv(values: List):
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

    return most





if __name__ == '__main__':

    if len(sys.argv) > 1:
        input_path = Path(sys.argv[1])
    else:
        input_path = Path('input.txt')

    main(input_path)
