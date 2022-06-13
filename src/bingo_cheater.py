marker = 'X'

def fast_process_data():
    with open('data/bingo_input.txt', 'r') as bingo:
        numbers, *boards = bingo.read().split('\n\n')
        numbers = [int(number) for number in numbers.split(',')]
        all_boards = [[[int(col) for col in row.split()] for row in board.split('\n')] for board in boards]
    return numbers, all_boards


def do_sum(table):
    sum = 0
    for row in table:
        for number in row:
            if number != marker:
                sum += number
    return sum


def fast_marking(number, board):
    for row in board:
        for column in range(0, len(row)):
            if row[column] == number:
                row[column] = marker


def fast_check(board):
    winner = False

    for row in board:
        winner = all(element in [marker] for element in row)
        if winner:
            return winner
    
    for i in range(0, len(board[0])):
        winner = all(element in [marker] for element in [row[i] for row in board])
        if winner:
            return winner
    
    return winner


def first_to_win():
    numbers, boards = fast_process_data()
    for number in numbers:
        for board in boards:
            fast_marking(number, board)
            if fast_check(board):
                sum = do_sum(board)
                score = sum * number
                print(f'\n-----------------------------------------------------\nFinal sum: {sum}\nWinning number: {number}\nWinning score: {score}')
                return score


def last_to_win():
    numbers, boards = fast_process_data()
    winner = False
    while not winner:
        number = numbers[0]
        numbers = numbers[1:]
        
        for board in boards:
            fast_marking(number, board)
        
        index = 0
        while index < len(boards):
            board = boards[index]
            if fast_check(board):
                if len(boards) > 1:
                    boards.pop(index)
                else:
                    winner = True
                    index = len(boards) + 1
                    sum = do_sum(board)
                    score = sum * number
                    print(f'\n-----------------------------------------------------\nFinal sum: {sum}\nFinal number: {number}\nLosing score: {score}')
            else:
                index += 1


def main():
    first_to_win()
    last_to_win()


if __name__ == '__main__':
    main()

