from typing import List
from pathlib import Path
import sys

def main(input_path: Path):
    points = parse_data(input_path)

    min_p = min(points)
    max_p = max(points)
    smallest = None
    align_val = None
    for i in range(min_p, max_p + 1):
        dist = sum([abs(p - i) for p in points])
        if smallest is None or dist < smallest:
            smallest = dist
            align_val = i

    print('align_val', align_val)
    print('total fuel', smallest)


def parse_data(input_path: Path) -> List[int]: 
    
    with input_path.open() as infile:
        line = infile.read()
        
    return [int(point) for point in line.strip().split(',')]


if __name__ == '__main__':

    if len(sys.argv) > 1:
        input_path = Path(sys.argv[1])
    else:
        input_path = Path('input.txt')

    main(input_path)
