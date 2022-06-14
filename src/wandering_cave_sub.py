import re


def build_cave_map():
    with open('data/cave_system.txt', 'r') as raw:
        cave_system = {}
        for line in raw.readlines():
            node_a, node_b = line.split('-')
            node_a, node_b = node_a.strip(), node_b.strip()
            if node_a not in cave_system:
                cave_system[node_a] = [node_b]
            elif node_b not in cave_system[node_a]:
                cave_system[node_a].append(node_b)
            if node_b not in cave_system:
                cave_system[node_b] = [node_a]
            elif node_a not in cave_system[node_b]:
                cave_system[node_b].append(node_a)
        return cave_system


def find_paths_r(caves, key, visited, paths, queue, twice):
    copy_q = queue[:]
    copy_v = visited[:]
    copy_q.append(key)
    if re.search('[^A-Z]', key):
        copy_v.append(key)
    adj = caves[key]
    for i in range(len(adj)):
        cave = adj[i]
        if cave == 'end':
            copy_q.append(cave)
            paths.append(copy_q)
            continue
        elif cave not in visited:
            paths = find_paths_r(caves, cave, copy_v, paths, copy_q, twice)
        elif not (cave == 'start' or cave == 'end') and (twice is not None and not twice) and cave in visited:
            paths = find_paths_r(caves, cave, copy_v, paths, copy_q, True)
    return paths


def find_paths(caves, key, twice=None):
    queue = [key]
    paths = []
    visited = [key]
    adj = caves[key]
    for i in range(len(adj)):
        cave = adj[i]
        if cave != 'end':
            paths = find_paths_r(caves, cave, visited, paths, queue, twice)
    return paths


def main():
    cave_map = build_cave_map()
    paths = find_paths(cave_map, 'start')
    print(f'Paths single: {len(paths)}')
    paths = find_paths(cave_map, 'start', twice=False)
    print(f'Paths twice: {len(paths)}')


if __name__ == '__main__':
    main()

