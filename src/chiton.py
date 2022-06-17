from collections import defaultdict
import heapq


def get_map():
    with open('data/chiton_map.txt', 'r') as raw:
        matrix = [[int(col) for col in row] for row in raw.read().split('\n')]
        return matrix


def get_cost(graph, row, col, length, width):
    x = (graph[row % length][col % width] + (row // length) + (col // width))
    return (x - 1) % 9 + 1


def diijkstra(weighted_graph, full):
    length = len(weighted_graph) if not full else len(weighted_graph) * 5 # x, rows
    width = len(weighted_graph[0]) if not full else len(weighted_graph[0]) * 5 # y, cols

    costs = defaultdict(int) # Store costs here
    pq = [(0, 0, 0)] # Current options
    heapq.heapify(pq) # Make pq an actual priority q
    visited = set() # Visited nodes

    while pq:
        cost, row, col = heapq.heappop(pq)

        if (row, col) in visited:
            continue
        visited.add((row, col))

        costs[(row, col)] = cost

        if row == length - 1 and col == width - 1: # Reached point b
            return cost

        for row_d, col_d in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            adj_r = row + row_d
            adj_c = col + col_d

            in_range = (0 <= adj_r < length) and (0 <= adj_c < width)
            if not in_range:
                continue

            accum = weighted_graph[adj_r][adj_c] if not full else get_cost(weighted_graph, adj_r, adj_c, length // 5, width // 5)

            heapq.heappush(pq, (cost + accum, adj_r, adj_c))


def main():
    graph = get_map()
    cost = diijkstra(graph, False)
    print(f'Fastest path (cost-wise) to exit the cave is {cost} (Considering a fifth of the map)')
    cost = diijkstra(graph, True)
    print(f'Fastest path (cost-wise) to exit the cave is {cost} (Considering the whole map)')


if __name__ == '__main__':
    main()

