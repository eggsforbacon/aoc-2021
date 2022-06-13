def find_edge(lines):
    edge = [0, 0]
    for line in lines:
        for coords in line:
            for num in range(0, 2):
                if coords[num] > edge[num]:
                    edge[num] = coords[num]
    edge[0] += 1
    edge[1] += 1
    return edge


def draw_line(diagram, horizontal, vertical, pt_from, pt_to, diagonal):

    current = pt_from
    line_is_diagonal = horizontal != 0 and vertical != 0
    if not diagonal and line_is_diagonal:
        return diagram
    while True:
        x = current[1]
        y = current[0]
        diagram[x][y] += 1
        if current == pt_to:
            return diagram
        current[0] += horizontal
        current[1] += vertical


def draw_lines(diagram, lines, diagonal):
    for line in lines:
        coord_from = line[0]
        coord_to = line[1]
        direction_x = 1 if coord_from[0] < coord_to[0] else -1 if coord_from[0] > coord_to[0] else 0
        direction_y = 1 if coord_from[1] < coord_to[1] else -1 if coord_from[1] > coord_to[1] else 0
        diagram = draw_line(diagram, direction_x, direction_y, coord_from, coord_to, diagonal)
    return diagram


def read_coords(diagonal):
    with open('data/test/vent_coords.txt', 'r') as file:
        lines = file.read().split('\n')
        lines = [[[int(coord) for coord in coords.split(',')] for coords in line.split(' -> ')] for line in lines]
        edge = find_edge(lines)
        diagram = [[0 for _ in range(0, edge[1])] for _ in range(0, edge[0])]
        diagram = draw_lines(diagram, lines, diagonal)
        return diagram


def count_max_overlaps(diagram):
    threshold = 2
    count = 0
    global_max = threshold
    for row in diagram:
        local_max = max(row)
        if local_max >= threshold:
            global_max = local_max if local_max > global_max else global_max
            count += len([elem for elem in row if elem >= threshold])
    return global_max, count


def main():
    diagram = read_coords(False)
    max, count = count_max_overlaps(diagram)
    print(f'Max overlapping lines in a given point (excluding diagonals): {max}\nOccurring {count} times')
    diagram = read_coords(True)
    max, count = count_max_overlaps(diagram)
    print(f'Max overlapping lines in a given point (including diagonals): {max}\nOccurring {count} times')


if __name__ == '__main__':
    main()

