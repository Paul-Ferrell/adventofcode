from typing import List, Tuple
from pathlib import Path
import sys


class Cell:
    def __init__(self, value: int):
        self.value = value
        self.picked = False

    def __str__(self):
        if self.picked:
            return '\x1b[32m{:2d}\x1b[0m'.format(self.value)
        else:
            return '{:2d}'.format(self.value)

    def __repr__(self):
        return "Cell({})".format(self)


class Board:
    def __init__(self, rows: List[List[int]]):
        self.rows = []
        for row in rows:
            new_row = []
            for val in row:
                new_row.append(Cell(val))
            self.rows.append(new_row)

        self.cols = [[None for i in range(5)] for j in range(5)]
        for r in range(len(self.rows)):
            for c in range(len(self.rows[r])):
                self.cols[c][r] = self.rows[r][c]

    def __str__(self):
        return "\n".join([" ".join([str(cell) for cell in row]) for row in self.rows])+'\n'

    def mark(self, picked: int):
        """Check if one of the cells has the given value, and mark it."""

        for row in self.rows:
            for cell in row:
                if cell.value == picked:
                    cell.picked = True
                    return


    def is_winner(self) -> bool:
        """Return true if this board has a winning row/col."""

        for row in self.rows:
            if all([cell.picked for cell in row]):
                return True

        for col in self.cols:
            if all([cell.picked for cell in col]):
                return True

        return False

    def score(self) -> int:
        """Return the total of all unpicked cells."""

        total = 0
        for row in self.rows:
            for cell in row:
                if not cell.picked:
                    total += cell.value

        return total


def main(input_path: Path):
    
    picked, boards = parse_data(input_path)

    num, board = find_loser(picked, boards)

    if num is None:
        print("No winner")
    else:
        print("WINNER!")
        print(board)
        print('score:', num * board.score())


def find_loser(picked: List[int], boards: List[Board]) -> Tuple[int, Board]:
    boards = list(boards)

    for num in picked:
        finished = []
        for i in range(len(boards)):

            board = boards[i]
            board.mark(num)

            if board.is_winner():
                finished.append(board)
                boards[i] = None

        boards = list(filter(lambda b: b is not None, boards))
        print('boards', len(boards))
        if not boards:
            break

    return num, finished[-1]



def parse_data(input_path) -> Tuple[List[int], List[Board]]:
    """Return the picked numbers and list of Boards."""

    with input_path.open() as infile:
        picked = infile.readline()
        picked = [int(num) for num in picked.split(',')]
        infile.readline()

        boards = []
        board = []
        for line in infile:
            line = line.strip()
            if not line:
                boards.append(Board(board))
                board = []
            else:
                nums = [int(num) for num in line.split()]
                board.append(nums)

        if board:
            boards.append(Board(board))

    return  picked, boards


if __name__ == '__main__':

    if len(sys.argv) > 1:
        input_path = Path(sys.argv[1])
    else:
        input_path = Path('input.txt')

    main(input_path)
