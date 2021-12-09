from typing import List
from pathlib import Path
from collections import defaultdict
import sys

def main(input_path: Path):

    lines = parse_data(input_path)
    

    danger_zone = defaultdict(lambda: 0)
    for line in lines:
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
    if start[0] < end[0]: 
        xslope = 1
    elif start[0] == end[0]:
        xslope = 0
    else:
        xslope = -1

    if start[1] < end[1]:
        yslope = 1
    elif start[1] == end[1]:
        yslope = 0
    else:
        yslope = -1

    xpos, ypos = start
    while (xpos, ypos) != end:
        points.append((xpos, ypos))
        xpos += xslope
        ypos += yslope
    points.append(end)

    return points


def parse_data(input_path):
    data = []

    with input_path.open() as infile:
        for line in infile:
            line = line.strip()
            start, _, end = line.split()
            start = tuple(int(val) for val in start.split(','))
            end = tuple(int(val) for val in end.split(','))

            data.append((start, end))

    return data


if __name__ == '__main__':

    if len(sys.argv) > 1:
        input_path = Path(sys.argv[1])
    else:
        input_path = Path('input.txt')

    main(input_path)
