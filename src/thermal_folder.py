from pprint import pprint
import re


def map_instructions():
    with open('data/thermal_instructions.txt', 'r') as raw:
        coords = []
        folds = []
        lines = [line.strip() for line in raw.readlines()]
        for line in lines:
            if line == '':
                ind = lines.index(line)
                folds = [[el for el in re.sub('fold along ', '', instr).split('=')] for instr in lines[ind + 1:]]
                coords = {tuple(i) for i in [[int(num) for num in coord.split(',')] for coord in lines[:ind]]}
                break
        return coords, folds


def map_coords(coords):
    height, lenght = max( [int(pair[1]) for pair in coords] ) + 1, max( [int(pair[0]) for pair in coords] ) + 1
    mapped_coords = ''
    for y in range(height):
        for x in range(lenght):
            # print(f'{(x, y)} in {coords} => {(x, y) in coords}')
            mapped_coords += '# ' if (x, y) in coords else '  '
        mapped_coords += '\n'
    return mapped_coords


def do_folds(coords, folds):
    for i in range(len(folds)):
        instruction = folds[i]
        coords = fast_fold(instruction[0], int(instruction[1]), coords)
    return coords


def reflect(about, orientation, coord):
    if orientation == 'x':
        substract = 2 * about - coord[0]
        return [substract, coord[1]]
    elif orientation == 'y':
        susbtract =  2 * about - coord[1]
        return [coord[0], susbtract]
    return coord


def fast_fold(orientation, position, coords):
    new_set = {}
    if orientation == 'x':
        new_set = {coord for coord in coords if coord[0] < position}
        folded_half = {tuple(i) for i in [reflect(position, orientation, coord) for coord in coords if coord[0] > position]}
    elif orientation == 'y':
        new_set = {coord for coord in coords if coord[1] < position}
        folded_half = {tuple(i) for i in [reflect(position, orientation, coord) for coord in coords if coord[1] > position]}
    else:
        return None
    for i in folded_half:
        new_set.add(i)
    return new_set
            

def main():
    coords, folds = map_instructions()
    coords = do_folds(coords, folds)
    mapped = map_coords(coords)
    print(mapped)
    

if __name__ == '__main__':
    main()

