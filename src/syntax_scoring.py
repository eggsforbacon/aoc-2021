from pprint import pprint

def get_syntax():
    with open('data/navi_syntax.txt', 'r') as raw:
        syntax = [[character for character in line.strip()] for line in raw.readlines()]
        return syntax


def closes(closer, opener, key):
    if opener is None:
        return False
    try:
        return key[opener] == closer
    except:
        return False


# This function is a mess, I should have just done two separate functions
def check_wronglines(syntax, incomplete=False):
    height = len(syntax)
    key = {'(':')', '[':']', '{':'}', '<':'>'}
    openers = list(key.keys())
    scores = {')': 3, ']': 57, '}': 1197, '>': 25137} if not incomplete else {')': 1, ']': 2, '}': 3, '>': 4}
    score, multiplier = 0, 5
    if incomplete:
        score_list = []
        corrupted = False
    for x in range(height):
        line = syntax[x]
        length = len(line)
        opened = [None]
        for y in range(length):
            current = syntax[x][y]
            previous = opened[-1]
            if current in openers:
                opened.append(current)
                continue
            elif closes(current, previous, key):
                opened.pop()
                continue
            score += scores[current] if not incomplete else score
            if incomplete:
                corrupted = True
            break
        if incomplete:
            opened.reverse()
            for x in range(len(opened)):
                unclosed = opened[x]
                if unclosed is None:
                    break
                score = (score * multiplier) +  scores[key[unclosed]]
            if not corrupted:
                score_list.append(score)
            score = 0
        corrupted = False
    return score if not incomplete else sorted(score_list)[-((len(score_list)//2) + 1)]  


def main():
    syntax = get_syntax()
    score = check_wronglines(syntax)
    print(score)
    score = check_wronglines(syntax, incomplete=True)
    print(score)


if __name__ == '__main__':
    main()

