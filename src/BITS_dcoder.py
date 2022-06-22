from asyncio.subprocess import SubprocessStreamProtocol


def to_bin(i, base):
    converted = bin(int(i, base))[2:]
    if len(converted) < 4:
        converted = (converted[::-1] + '0'*(4 - len(converted)))[::-1]
    return converted


def d_code(string):
    decoded = ''
    for c in string:
        decoded += to_bin(c, 16)
    return decoded


def get_broadcast():
    with open('data/BITS_stream.txt', 'r') as stream:
        return d_code(stream.read())


def parse(packet, count=-1):
    if packet == '' or int(packet, 2) == 0:
        return 0
    if count == 0:
        return parse(packet)
    
    version = int(packet[:3], 2)
    typeID = int(packet[3:6], 2)
    is_literal = typeID == 4
    if is_literal:
        end = False
        head, tail = 6, 11
        while not end:
            end = packet[head] == '0'
            head = tail
            tail = head + 5
        return version + parse(packet[head:], -1)
    lengthID = packet[6]
    # Length
    if lengthID == '0':
        L = int(packet[7:22], 2)
        return version + parse(packet[22:22+L], -1) + parse(packet[22+L:], count - 1)
    # Number
    else:
        n = int(packet[7:18])
        return version + parse(packet[18:], n)


def operate(id_, values):
    if id_ == 0:
        return sum(values)
    if id_ == 1:
        p = 1
        for v in values:
            p *= v
        return p
    assert len(values) == 2, f'{values} is not len(2) on {id_}'
    if id_ == 2:
        return min(values)
    if id_ == 3:
        return max(values)
    if id_ == 5:
        return int(values[0] > values[1])
    if id_ == 6:
        return int(values[0] < values[1])
    if id_ == 7:
        return int(values[0] == values[1])


def parse_faster(broadcast, i, j=-1):
    if i > len(broadcast) - 4 or i == j:
        return None, None
    
    version = int(broadcast[i:i+3], base=2)
    typeID = int(broadcast[i+3:i+6], base=2)
    number = ''
    if version == 4:
        i += 6
        end = False
        while not end:
            if broadcast[i] == '0':
                end = True
            number += broadcast[i+1:i+5]
            i += 5
        
        return int(number, base=2), i

    subpackets = []
    next_start = None

    lenID = broadcast[i+6]
    
    if lenID == '0':
        L = int(broadcast[i+7:i+22], base=2)
        end = i + 22 + L
        index = i + 22
        prev_index = None
        while index != None:
            prev_index = index
            x, index = parse_faster(broadcast, index, j=end)
            subpackets.append(x)
        subpackets = subpackets[:-1]
        next_start = prev_index
    else:
        rem_sub_packs = int(broadcast[i+7:i+18], base=2)
        index = i + 18
        while rem_sub_packs > 0:
            x, index = parse_faster(broadcast, index)
            rem_sub_packs -= 1
            subpackets.append(x)
        next_start = index
    return operate(typeID, subpackets), next_start

def main():
    broadcast = get_broadcast()
    print(f'Version sum is: {parse(broadcast)}')
    print(f'Data sum is: {parse_faster(broadcast, 0)}')
    pass


if __name__ == '__main__':
    main()

