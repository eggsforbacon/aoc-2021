def read_heightmap():
    with open('data/heightmap.txt', 'r') as raw:
        heightmap = [[int(height) for height in line] for line in raw.read().split('\n')]
        return heightmap


def find_adjacents(map, height, length, x, y):
    adj = {}
    right = y + 1 if y < length - 1 else None
    left = y - 1 if y > 0 else None
    down = x + 1 if x < height - 1 else None
    up = x - 1 if x > 0 else None

    if right is not None:
        adj[f'{x}, {right}'] = map[x][right]
    if left is not None:
        adj[f'{x}, {left}'] = map[x][left]
    if down is not None:
        adj[f'{down}, {y}'] = map[down][y]
    if up is not None:
        adj[f'{up}, {y}'] = map[up][y]
    
    return adj


def find_low_points(heightmap):
    height = len(heightmap)
    length = len(heightmap[0])
    low_points = {}
    for x in range(height):
        for y in range(length):
            coord = heightmap[x][y]
            values = list((find_adjacents(heightmap, height, length, x, y)).values())
            extreme_adjacent = min(values)
            if coord < extreme_adjacent:
                key = f'{x}, {y}'
                low_points[key] = coord
    return low_points


def risk_level(points):
    risk = 0
    values = list(points.values())
    for val in values:
        risk += int(val) + 1
    return risk


def to_graph(heightmap, lenght, height):
    adjacents = {}
    adj_values = {}
    for x in range(height):
        for y in range(lenght):
            adj = find_adjacents(heightmap, height, lenght, x, y)
            adjacents[f'{x}, {y}'] = list(adj.keys())
            adj_values[f'{x}, {y}'] = list(adj.values())
    return adjacents


def find_basin(node, graph, map, visited):
    if node not in visited:
        visited.append(node)
    neighbors = graph[node]

    for n in neighbors:
        coord = [int(num) for num in n.split(',')]
        value = map[coord[0]][coord[1]]
        if value == 9:
            continue
        if n not in visited:
            visited.append(n)
            visited = find_basin(n, graph, map, visited)
    return visited


def basins(heightmap, points):
    keys = list(points.keys())
    height = len(heightmap)
    length = len(heightmap[0])
    low_points = [key for key in keys]
    basin_list = []
    graph = to_graph(heightmap, length, height)
    
    for node in low_points:
        basin = 0
        basin = find_basin(node, graph, heightmap, [])
        basin_lenght = len(basin)
        basin_list.append(basin_lenght)
    
    basin_list = sorted(basin_list)
    return basin_list[-1] * basin_list[-2] * basin_list[-3]


def main():
    heightmap = read_heightmap()
    points = find_low_points(heightmap)
    risk = risk_level(points)
    basin = basins(heightmap, points)
    print(f'Risk level: {risk}\nBasin index: {basin}')


if __name__ == '__main__':
    main()

