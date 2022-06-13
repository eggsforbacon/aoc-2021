def calc_gamma():
    gamma = ''
    with open('data/diagnostic.txt', 'r') as diag:
        bit = diag.readline().strip()
        bit_len = len(bit)
        tracker = [0] * bit_len
        eof = len(bit) == 0
        lines = 0

        while not eof:
            lines += 1
            i = 0
            for digit in bit:
                if digit == '1':
                    tracker[i] += 1
                i += 1

            bit = diag.readline().strip()
            eof = len(bit) == 0

        lines //= 2
        for digit in tracker:
            if digit > lines:
                gamma += '1'
            elif digit < lines:
                gamma += '0'
        
    return gamma


def calc_epsilon(gamma):
    epsilon = ''
    for digit in gamma:
        if digit == '1':
            epsilon += '0'
        else:
            epsilon += '1'
    
    return epsilon


def calc_level(readings, bit_criteria, depth):
    ones = []
    zeros = []
    if len(readings) == 1:
        return int(readings[0], 2)
    else:
        for line in readings:
            if line[depth] == '1':
                ones.append(line)
            else:
                zeros.append(line)
        ones_ = len(ones)
        zeros_ = len(zeros)

        flag_equal = ones_ == zeros_
        flag_ones = ones_ > zeros_

        if (flag_equal or flag_ones) and bit_criteria:
            return calc_level(ones, bit_criteria, (depth + 1)) # equal and O2 === ones and O2 (1)
        elif (flag_equal or flag_ones) and not bit_criteria:
            return calc_level(zeros, bit_criteria, (depth + 1)) # equal and CO2 === ones and CO2 (2)
        elif not flag_ones and bit_criteria:
            return calc_level(zeros, bit_criteria, (depth + 1)) # zeros and O2 === ¬ones and O2 (3)
        elif not flag_ones and not bit_criteria:
            return calc_level(ones, bit_criteria, (depth + 1)) # zeros and CO2 === ¬ones and CO2 (4)


def driver(criteria):
    with open('data/diagnostic.txt', 'r') as diag:
        return calc_level(diag.readlines(), criteria, 0)


def main():
    gamma = calc_gamma()
    epsilon = int(calc_epsilon(gamma), 2)
    gamma = int(gamma, 2)

    print(f'Gamma: {gamma}\nEpsilon: {epsilon}\nPower Consumption: {gamma * epsilon}')

    o2 = driver(True)
    co2 = driver(False)
    print(f'O2: {o2}\nCO2: {co2}\nLife support rating: {o2 * co2}')


if __name__ == '__main__':
    main()

