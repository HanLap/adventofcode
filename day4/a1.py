from functools import reduce

def parse_line(line):
    return [(int(line[i:i+2]), False) for i in range(0, len(line), 3)]

def parse_input():
    with open('input', 'r') as input:
        draws = list(map(
            lambda i: int(i), 
            input
                .readline()
                .replace('\n', '')
                .split(',')
        ))
        input.readline()
        boards = []
        i = 0
        board = []
        for line in input.readlines():
            if i >= 5:
                i = 0
                boards.append(board)
                board = []
            else:
                board.append(parse_line(line.replace('\n', '')))
                i += 1


        return (draws, boards)

def print_boards(boards):
    for board in boards:
        for line in board:
            print(line)
        print('\n')


def apply_nr(drawn, boards):
    for board in boards:
        for line in board:
            for i in range(len(line)):
                nr, _ = line[i]
                if nr == drawn:
                    line[i] = (nr, True) 

def check_if_board_won(board):
    # check row
    for line in board:
        if reduce(lambda acc, col: acc and col[1], line, True):
            return True
    # check column
    for i in range(len(board)):
        won = True
        for j in range(len(board[i])):
            _, marked = board[j][i]
            if not marked:
                won = False
        if won:
            return True
    return False

def calculate_score(drawn, board):
    flat = [col for line in board for col in line]

    unmarked = reduce(lambda acc, col: acc + col[0] if not col[1] else acc, flat, 0)
    print(unmarked)
    return unmarked * drawn


def main():
    draws, boards = parse_input()

    draw_history = []
    for drawn in draws:
        draw_history.append(drawn)
        apply_nr(drawn, boards)

        for board in boards:
            if check_if_board_won(board):
                print(draw_history)
                print("board won:")
                print_boards([board])
                print(drawn)
                print(calculate_score(drawn, board))
                return

    print_boards(boards)


main()