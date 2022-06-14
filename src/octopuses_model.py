from pprint import pprint
from typing import Generator


def get_map():
    with open('data/octopuses.txt', 'r') as raw:
        octi_map = {}
        for y, line in enumerate(raw.readlines()):
            for x, energy in enumerate(line.strip()):
                octi_map[x, y] = int(energy)
        return octi_map

def adjacent(x, y):
    for x_d in (-1, 0, 1):
        for y_d in (-1, 0, 1):
            if x_d == y_d == 0:
                continue
            yield x + x_d, y + y_d


def sequencer(octi):
    flashes = 0
    flash = []

    # step 1
    for key, val in octi.items():
        octi[key] += 1
        if octi[key] > 9:
            flash.append(key)
    
    # step 2
    while flash:
        point = flash.pop()
        if octi[point] == 0:
            continue
        
        octi[point] = 0
        flashes += 1

        for adj in adjacent(*point):
            if adj in octi and octi[adj] != 0:
                octi[adj] += 1
                if octi[adj] > 9:
                    flash.append(adj)
    
    return octi, flashes


def main():
    octi = get_map()
    flashes = 0
    lap = 100
    i = 0
    while i < lap:
        octi, fl = sequencer(octi)
        flashes += fl
        if fl == len(octi):
            print(f'All flashed in step {i + 1}')
            lap = i + 1
            break
        else:
            lap += 1
        i += 1
    print(f'Flashed {flashes} times in {lap} steps')


if __name__ == '__main__':
    main()

