from pathlib import Path
from typing import List, Tuple, NewType
import sys

def main(input_path: Path):

    commands = parse_movement(input_path)

    pos = navigate(commands, (0, 0, 0))

    print(pos)
    print(pos[0]*pos[1])

FORWARD = 'forward'
DOWN = 'down'
UP = 'up'

class Command:
    def __init__(self, direction: str, distance: int):
        self.direction = direction
        self.distance = distance


def parse_movement(path: Path) -> List[Command]:

    commands = []
    
    with path.open() as input_file:
        for line in input_file:
            line = line.strip()
            if not line:
                continue

            parts = line.split()
            if len(parts) != 2:
                continue

            direction, distance = parts
            try:
                distance = int(distance)
            except ValueError:
                print("Invalid distance: {}".format(line))
                break

            commands.append(Command(direction, distance))

    return commands

def navigate(commands: List[Command], start_pos: Tuple[int,int,int] = (0,0,0)) \
        -> Tuple[int, int, int]:

    x, depth, aim = start_pos

    for command in commands:
        if command.direction == UP:
            aim -= command.distance
        elif command.direction == DOWN:
            aim += command.distance
        elif command.direction == FORWARD:
            x += command.distance
            depth += command.distance * aim

    return x, depth, aim
    
if __name__ == '__main__':

    if len(sys.argv) > 1:
        input_file = Path(sys.argv[1])
    else:
        input_file = Path('input.txt')

    if not input_file.exists():
        print("No such imput file:", input_file)
    else:
        main(input_file)
