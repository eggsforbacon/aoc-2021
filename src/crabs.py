def get_positions():
    with open('data/horizontal_positions.txt', 'r') as raw:
        positions = [int(pos) for pos in raw.read().strip().split(',')]
        return positions


def factorial_sum(n):
    return n * (n+1) // 2


def least_fuel(fi):
    positions = get_positions()
    crab_map = {}
    for pos in positions:
        if pos not in crab_map:
            crab_map[pos] = 0
        crab_map[pos] += 1
    less_gas = float('inf')
    pos = -1
    ceil = len(crab_map.keys())
    for x in range(ceil):
        gas = 0
        for i, count in crab_map.items():
            delta = abs(x - i) if not fi else factorial_sum(abs(x - i))
            gas += delta * count
        if gas <= less_gas:
            pos = x
            less_gas = gas
    return less_gas, pos


def main():
    gas, position = least_fuel(False)
    print(f'{gas} fuel required to align crabs to {position}')
    gas, position = least_fuel(True)
    print(f'{gas} fuel required to align crabs to {position}')


if __name__ == '__main__':
    main()

