from pprint import pprint


LEN_1, LEN_4, LEN_7, LEN_8 = 2, 4, 3, 7


def notes():
    with open('data/segment_notes.txt', 'r') as raw:
        all_notes = [line.strip() for line in raw.readlines()]
        signals = [[signal for signal in line.split('|')[0].split()] for line in all_notes] # Holy shit man
        outputs = [[output for output in line.split('|')[1].split()] for line in all_notes] # list comprehensions are awesome :D
        return signals, outputs


def count_typeA_segs(outputs):
    count = 0
    for put in outputs:
        for number in put:
            line_length = len(number)
            if line_length == LEN_1 or line_length == LEN_4 or line_length == LEN_7 or line_length == LEN_8:
                count += 1
    return count


def define_codices(signals):
    codices = []
    for signal in signals:
        signal = sorted(signal, key=len)
        codex = {}

        # Find one, seven, four and eight by length
        one = signal[0]
        seven = signal[1]
        four = signal[2]
        eight = signal[9]

        signal = signal[3:9]

        six_segments = [seg for seg in signal if len(seg) == 6]
        five_segments = [seg for seg in signal if len(seg) == 5]
        
        # Find six with one
        six = [seg for seg in six_segments if one[0] not in seg or one[1] not in seg][0]

        # Sort one in the right order
        flipped = one[0] in six
        if flipped:
            one = one[::-1]

        # Find three, two and five with sorted one
        three = [seg for seg in five_segments if one[0] in seg and one[1] in seg][0]
        two = [seg for seg in five_segments if one[0] in seg and one[1] not in seg][0]
        five = [seg for seg in five_segments if one[1] in seg and one[0] not in seg][0]

        # Find 9 and 0 with 3 and 7 shenanigans
        sym_3diff7 = list(set(three) - set(seven))
        six_segments.remove(six)
        nine = [seg for seg in six_segments if sym_3diff7[0] in seg and sym_3diff7[1] in seg][0]
        six_segments.remove(nine)
        zero = six_segments[0]

        # Add them :D
        codex['0'] = sorted(zero)
        codex['1'] = sorted(one)
        codex['2'] = sorted(two)
        codex['3'] = sorted(three)
        codex['4'] = sorted(four)
        codex['5'] = sorted(five)
        codex['6'] = sorted(six)
        codex['7'] = sorted(seven)
        codex['8'] = sorted(eight)
        codex['9'] = sorted(nine)

        codices.append(codex)
    return codices


def decode_outputs(codices, outputs):
    decoded_outputs = []
    for index in range(len(outputs)):
        output = outputs[index]
        keys = list(codices[index].keys())
        values = list(codices[index].values())
        decoded_output = ''
        for coded in output:
            number = keys[values.index(sorted(coded))]
            decoded_output += number
        decoded_outputs.append(decoded_output)
    return decoded_outputs


def main():
    signals, outputs = notes()
    
    # Part 1
    countA = count_typeA_segs(outputs)
    print (f'{countA} unique-length segments in output stream')

    # Part 2
    codices = define_codices(signals)
    decoded_outputs = decode_outputs(codices, outputs)
    addall = sum([int(num) for num in decoded_outputs])
    print(f'The sum of all the numbers is {addall}')


if __name__ == '__main__':
    main()

