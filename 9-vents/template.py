from typing import List
from pathlib import Path
import sys

def main(input_path: Path):
    pass


if __name__ == '__main__':

    if len(sys.argv) > 1:
        input_path = Path(sys.argv[1])
    else:
        input_path = Path('input.txt')

    main(input_path
