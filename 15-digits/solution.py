from typing import List, Set, Tuple, NewType
from pathlib import Path
import sys


DSet = NewType('DSet', Set[str])


def main(input_path: Path):

    displays = parse_data(input_path)

    total_1478 = 0
    total = 0
    
    for keys, digits in displays:
        
        decoder = decode_display(keys)

        code = ''.join(decoder[digit] for digit in digits)

        total_1478 += code.count('1')
        total_1478 += code.count('4')
        total_1478 += code.count('7')
        total_1478 += code.count('8')

        total += int(code)

    print('total', total_1478)
    print('sum', total)

def filter_by_len(keys, klen):
    matching = []

    for key in keys:
        if len(key) == klen:
            matching.append(key)

    return matching

def decode_display(keys: List[DSet]):

    d1 = filter_by_len(keys, 2)[0]
    d7 = filter_by_len(keys, 3)[0]
    d4 = filter_by_len(keys, 4)[0]
    d8 = filter_by_len(keys, 7)[0]
    d069 = filter_by_len(keys, 6)
    
    d0 = d6 = d9 = None
    BD = d4 - d7
    for key in d069:
        if len(key.intersection(d1)) == 1:
            d6 = key
        elif len(key.intersection(BD)) == 1:
            d0 = key
        else:
            d9 = key
    
    if None in (d0, d6, d9):
        raise ValueError

    d5 = d9.intersection(d6) 

    A = d7-d1
    D = BD - d0
    B = BD - D
    F = d1.intersection(d6)
    C = d1 - F
    E = d6 - d5
    G = d8 - (A|B|C|D|E|F)

    d2 = A|C|D|E|G
    d3 = A|C|D|F|G
    
    return {
        d0: '0',
        d1: '1',
        d2: '2',
        d3: '3',
        d4: '4',
        d5: '5',
        d6: '6',
        d7: '7',
        d8: '8',
        d9: '9'}


def parse_data(input_path: Path) -> List[Tuple[List[DSet], List[DSet]]]:
    displays = []

    with input_path.open() as infile:
        for line in infile:
            line = line.strip()
            if not line:
                continue
            
            keys, digits = line.split('|')
            keys = [frozenset(part) for part in keys.split()]
            digits = [frozenset(part) for part in digits.split()]
            
            displays.append((keys, digits))
    
    return displays


if __name__ == '__main__':

    if len(sys.argv) > 1:
        input_path = Path(sys.argv[1])
    else:
        input_path = Path('input.txt')

    main(input_path)
