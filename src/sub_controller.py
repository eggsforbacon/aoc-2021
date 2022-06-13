def forward(quantity, h_pos, v_pos = None, aim = None):
    result = h_pos + quantity
    if aim != None:
        result = [result, v_pos + aim*quantity]
    return result


def up(quantity, v_pos, aim = None):
    result = v_pos - quantity if aim == None else aim - quantity
    return result

def down(quantity, v_pos, aim = None):
    result = v_pos + quantity if aim == None else aim + quantity
    return result


def coord_product():

    h_pos = 0
    v_pos = 0

    with open('data/sub_route.txt', 'r') as route:
        instruction = route.readline().split()
        eof = len(instruction) == 0

        while not eof:
            direction = instruction[0]
            quantity = int(instruction[1])

            if direction == 'forward':
                h_pos = forward(quantity, h_pos)
            elif direction == 'up':
                v_pos = up(quantity, v_pos)
            elif direction == 'down':
                v_pos = down(quantity, v_pos)
            
            instruction = route.readline().split()
            eof = len(instruction) == 0

    return h_pos * v_pos


def coord_product_aim():

    h_pos = 0
    v_pos = 0
    aim = 0

    with open('data/sub_route.txt', 'r') as route:
        instruction = route.readline().split()
        eof = len(instruction) == 0
        
        while not eof:
            direction = instruction[0]
            quantity = int(instruction[1])

            if direction == 'forward':
                coords = forward(quantity, h_pos, v_pos, aim)
                h_pos = coords[0]
                v_pos = coords[1]
            elif direction == 'up':
                aim = up(quantity, v_pos, aim)
            elif direction == 'down':
                aim = down(quantity, v_pos, aim)
            
            instruction = route.readline().split()
            eof = len(instruction) == 0


    return h_pos * v_pos


def main():
    print(coord_product())
    print(coord_product_aim())
    pass

if __name__ == '__main__':
    main()

