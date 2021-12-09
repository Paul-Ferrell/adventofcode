from pathlib import Path
from typing import List, Tuple, NewType

def main(input_path: str):

    input_path = Path(input_path)

    commands = parse_movement(input_path)

    pos = navigate(commands, (0, 0, 0))

    print('final position', pos)
    print(pos[0]*pos[2])

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
    """Alter the current submarine position according to each command."""

    x, y, depth = start_pos

    for command in commands:
        if command.direction == UP:
            depth -= command.distance
        elif command.direction == DOWN:
            depth += command.distance
        elif command.direction == FORWARD:
            x += command.distance

    return x, y, depth
    
if __name__ == '__main__':

    main('input.txt')
    



