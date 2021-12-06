from pathlib import Path
from typing import List

def parse_data(path: Path) -> List[int]:
    """Parse the data file, which should be a newline separated set of ints."""

    data = []
    with path.open() as data_file: 
        for line in data_file:
            line = line.strip()
            if line:
                try:
                    point = int(line)
                except ValueError:
                    continue

                data.append(point)

    return data


def rolling_sum(data: List[int], window_size: int = 3) -> List[int]:
    """Return a list of rolling averages given the input file of the given window size."""

    sums = []
    windows = []

    for point in data:
        for window in windows:
            window.append(point)
        windows.append([point])

        if len(windows[0]) == window_size:
            sums.append(sum(windows.pop(0)))

    return sums


def get_increases(data: List[int]) -> int:
    """Return the number of times a number in the given list is larger than the 
    previous number."""

    last = None
    increases = 0
    for point in data:
        if last is not None:
            if point > last:
                increases += 1

        last = point

    return increases

DATA_PATH = Path('input.txt')

if __name__ == '__main__':
    data = parse_data(DATA_PATH)
    data = rolling_sum(data)
    increases = get_increases(data)

    print('increases', increases)
