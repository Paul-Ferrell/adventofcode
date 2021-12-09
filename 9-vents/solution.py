from typing import List
from pathlib import Path
from collections import defaultdict
import sys

def main(input_path: Path):

    lines = parse_data(input_path)
    
    vhlines = []
    for line in lines:
        start, end = line
        if start[0] == end[0] or start[1] == end[1]:
            vhlines.append(line)

    danger_zone = defaultdict(lambda: 0)
    for line in vhlines:
        points = get_points(line)
        for point in points:
            danger_zone[point] += 1

    danger_score = 0 
    for val in danger_zone.values():
        if val >= 2:
            danger_score += 1

    print('danger_score', danger_score)



def get_points(line):
    """Return a list of points that this line crosses."""

    points = []

    start, end = line
    if start[0] > end[0] or start[1] > end[1]: 
        start, end = end, start

    for x in range(start[0], end[0]+1):
        for y in range(start[1], end[1]+1):
            points.append((x,y))

    return points


def parse_data(input_path):
    data = []

    with input_path.open() as infile:
        for line in infile:
            line = line.strip()
            start, _, end = line.split()
            start = [int(val) for val in start.split(',')]
            end = [int(val) for val in end.split(',')]

            data.append((start, end))

    return data


if __name__ == '__main__':

    if len(sys.argv) > 1:
        input_path = Path(sys.argv[1])
    else:
        input_path = Path('input.txt')

    main(input_path)
