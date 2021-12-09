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

    @property
    def neighbors(self) -> List["Point"]:
        """Return all non-null orthogonal neighbors."""

        neighbors = []
        for neighbor in self.left, self.up, self.right, self.down:
            if neighbor is not None:
                neighbors.append(neighbor)
        return neighbors


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

    def basins(self) -> List[List[Point]]:
        """Return a list of basins, lists of nodes that flow down to a single low point. 
        Due to the nature of the data, no node can flow to multiple low points, which simplifies
        things."""

        basins = []
        for low_point in self.low_points():
            basins.append(self._basin_search(low_point))

        return basins

    def _basin_search(self, low_point: Point) -> List[Point]:
        """Find all the points that are in the basin with the given low point. A 
        point is in a basin if all its lower (orthogonal) neighbors are also in 
        the basin, and all other points are higher. Because of the simplification of the
        data a point is in the basin if it neighbors a point in the basin and it isn't 
        height 9."""
 
        level = low_point.height + 1 
        prospects = low_point.neighbors

        basin = {low_point}

        seen = []

        while prospects:
            prospect = prospects.pop(0)
            seen.append(prospect)
            if prospect.height != 9:
                for neigh in prospect.neighbors:
                    if neigh not in basin and neigh not in seen:
                        prospects.append(neigh)
                basin.add(prospect)

        return list(basin)

    def __str__(self):
        """Return a visualization of the heightmap."""

        low_points = self.low_points()

        point = self.ul_point
        next_row = point.down

        out = []
        basins = self.basins()

        while next_row is not None:
            next_row = point.down
            while point is not None:
                if point in low_points:
                    out.append("\x1b[32m{}\x1b[0m".format(point.height))
                elif point in low_points:
                    out.append("\x1b[2m{}\x1b[0m".format(point.height))
                else:
                    basin_count = 0
                    for basin in basins:
                        if point in basin:
                            basin_count += 1

                    if basin_count > 1:
                        out.append("\x1b[31m{}\x1b[0m".format(point.height))
                    elif basin_count == 1:
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

    basins = height_map.basins()
    basins.sort(key=lambda k: len(k))

    top3_sizes = [len(basin) for basin in basins[-3:]]
    answer = 1
    for s in top3_sizes:
        answer *= s
    print('top3 sizes', top3_sizes)
    print('answer', answer)




    



if __name__ == '__main__':

    if len(sys.argv) > 1:
        input_path = Path(sys.argv[1])
    else:
        input_path = Path('input.txt')

    main(input_path)
