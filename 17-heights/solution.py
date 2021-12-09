from typing import List
from pathlib import Path
import sys


class Point:
    """Represents a point on the map."""
    
    def __init__(self, height):
        
        self.height = height
        self.left = None
        self.right = None
        self.up = None
        self.down = None

    @property
    def risk_level(self):
        return self.height + 1


class Map:
    def __init__(self, raw_map: List[List[int]]):

        self.points = self.init_points(raw_map)
        self.ul_point = self.points[0]


    def init_points(self, raw_map: List[List[int]]) -> List[Point]:

        all_points = []
 
        prev_row = None
        for row in raw_map:
            prev_point = None
            for raw_point in row:
                point = Point(raw_point)
                if prev_point is not None:
                    point.left = prev_point
                    prev_point.right = point
                if prev_row is not None:
                    point.up = prev_row
                    prev_row.down = point
                    prev_row = prev_row.right

                prev_point = point
                all_points.append(point)
            
            prev_point = None
            prev_row = point
            while prev_row.left is not None:
                prev_row = prev_row.left

        print(len(all_points))
    
        return all_points

    def low_points(self) -> List[Point]:
        """Find all the points where their orthogonal neighbors are all higher."""

        low_points = []
        for point in self.points:
            for neighbor in point.left, point.right, point.up, point.down:
                if neighbor is not None and neighbor.height <= point.height:
                    break
            else:
                low_points.append(point)

        return low_points

    def __str__(self):
        """Return a visualization of the heightmap."""

        low_points = self.low_points()

        point = self.ul_point
        next_row = point.down

        out = []

        while next_row is not None:
            next_row = point.down
            while point is not None:
                if point in low_points:
                    out.append("\x1b[32m{}\x1b[0m".format(point.height))
                elif point.height == 9:
                    out.append("\x1b[33m{}\x1b[0m".format(point.height))
                else:
                    out.append(str(point.height))
                point = point.right
            point = next_row
            out.append('\n')
        
        return ''.join(out)


def parse_data(input_path: Path) -> List[List[int]]:
    
    data = []
    with input_path.open() as infile:
        for line in infile:
            row = [int(c) for c in line.strip()]
            data.append(row)

    return data


def main(input_path: Path):

    raw_map = parse_data(input_path)
    height_map = Map(raw_map)

    print(height_map)

    lowest = height_map.low_points()

    print('total_risk', sum([point.risk_level for point in lowest]))



if __name__ == '__main__':

    if len(sys.argv) > 1:
        input_path = Path(sys.argv[1])
    else:
        input_path = Path('input.txt')

    main(input_path)
