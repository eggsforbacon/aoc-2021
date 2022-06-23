import re


def map_target():
    with open('data/target_area.txt', 'r') as raw:
        string = re.sub('target area: ', '', raw.read())
        bounds = string.split(', ')
        x = [int(num) for num in bounds[0][2:].split('..')]
        y = [int(num) for num in bounds[1][2:].split('..')]
        return x, y


def reaches_target(velocity, target):
    x, y = 0, 0
    ymax = y
    xd, yd = velocity
    xf, yf = target
    reached = xf[0] <= x <= xf[1] and yf[0] <= y <= yf[1]
    out_bounds = x > xf[1] or y < yf[0]
    while not reached and not out_bounds:
        x += xd
        y += yd
        ymax = y if y >= ymax else ymax
        yd -= 1
        xd = xd - 1 if xd > 0 else xd + 1 if xd < 0 else xd
        reached = xf[0] <= x <= xf[1] and yf[0] <= y <= yf[1]
        out_bounds = x > xf[1] or y < yf[0]
    if out_bounds:
        ymax = None
    return ymax, [x, y]


def find_stylish(target):
    ymax = [0, None, None]
    posibilities = 0
    right_edge = target[0][1] + 1
    bottom_edge = target[1][0]*2
    for x in range(right_edge):
        for y in range(bottom_edge, -bottom_edge):
            velocity = [x, y]
            newy, lands = reaches_target(velocity, target)
            if newy is not None: 
                posibilities += 1
                if newy > ymax[0]:
                    ymax = [newy, velocity, lands]

    
    print(f'Max height {ymax[0]} is reached with starting velocity {ymax[1]} landing at point {ymax[2]}\n(Out of {posibilities} posibilities)')


def main():
    target = map_target()
    find_stylish(target)


if __name__ == '__main__':
    main()

