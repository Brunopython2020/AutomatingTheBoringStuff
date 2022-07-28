the_board = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}


turn = 'X'


def print_board(board):
    count_line = 0
    count_column = 0
    for v in board.values():
        if count_line < 2:
            print(v,end=' | ')
            count_line += 1
        elif count_line == 2:
            print(v,end='')
            count_line += 1
        if count_line == 3:
            print()
            count_column +=1
            if count_column < 3:
                for i in range(3):
                    print('---',end='')
            print()
            count_line = 0


def check_empty_board(move, board):
    if board[move] == ' ':
        return True
    else:
        return False


def board_input(board):
    while True:
        try:
            typed_move = input()
            if typed_move not in board.keys():
                print('This is not a valid move, please type again.')
            else:
                if check_empty_board(typed_move, board):
                    break
                else:
                    print('This movement is not valid, because the positon is occupied.\nPlease type again.')
        except Exception as e:
            print(f'We had an Error: {e}\nPlease Type a valid value.')

    return typed_move


def check_winner(move,board):

    if (board['top-L'] == board['top-M'] == board['top-R']) or (board['mid-L'] == board['mid-M'] == board['mid-R']) or (board['low-L'] == board['low-M'] == board['low-R']) or \
    (board['top-L'] == board['mid-L'] == board['low-L']) or (board['top-M'] == board['mid-M'] == board['low-M']) or (board['top-R'] == board['mid-R'] == board['low-R']) or \
        (board['top-L'] == board['mid-M'] == board['low-R']) or (board['top-R'] == board['mid-M'] == board['low-L']):

       pass

    if move == 'top-L' and ((board['top-L'] == board['top-M'] == board['top-R']) or (board['top-L'] == board['mid-L'] == board['low-L']) or (board['top-L'] == board['mid-M'] == board['low-R'])):
        return True
    
    elif move == 'top-M' and ((board['top-L'] == board['top-M'] == board['top-R']) or (board['top-M'] == board['mid-M'] == board['low-M'])):
        return True

    elif move == 'top-R' and ((board['top-R'] == board['top-M'] == board['top-L']) or (board['top-R'] == board['mid-R'] == board['low-R']) or (board['top-R'] == board['mid-M'] == board['low-L'])):

        return True

    elif move == 'mid-L' and ((board['top-L'] == board['mid-L'] == board['low-L']) or (board['mid-L'] == board['mid-M'] == board['mid-R'])):
        
        return True
    
    elif move == 'mid-M' and ((board['mid-L'] == board['mid-M'] == board['mid-R']) or (board['top-M'] == board['mid-M'] == board['low-M'])):

        return True

    elif move == 'mid-R' and ((board['mid-L'] == board['mid-M'] == board['mid-R']) or (board['top-R'] == board['mid-R'] == board['low-R'])):

        return True
    
    elif move == 'low-L' and ( (board['top-L'] == board['mid-L'] == board['low-L']) or  (board['low-L'] == board['low-M'] == board['low-R']) or (board['top-R'] == board['mid-M'] == board['low-L'])):

        return True
    elif move == 'low-M' and ( (board['low-L'] == board['low-M'] == board['low-R']) or  (board['top-M'] == board['mid-M'] == board['low-M'])):

        return True
    elif move == 'low-R' and ( (board['top-R'] == board['mid-R'] == board['low-R']) or  (board['low-L'] == board['low-M'] == board['low-R']) or (board['top-L'] == board['mid-M'] == board['low-R'])):

        return True
    else:
        return False


    




print_board(the_board)

for i in range(9):

    print(f'It is time for {turn} to play. Type the position: ')
    
    move = board_input(the_board)


    if turn == 'X':

        the_board[move] = 'X'

        winner = check_winner(move,the_board)

        if winner:
            print(f'Congratulations {turn} you are the WINNER!')
            print_board(the_board)
            break
        elif not winner and i == 8:
            print('The game was Draw!')
        turn = 'O'
        print_board(the_board)


    elif turn == 'O':

        the_board[move] = 'O'

        winner = check_winner(move,the_board)

        if winner:
            print(f'Congratulations {turn} you are the WINNER!')
            print_board(the_board)
            break
        elif not winner and i == 8:
            print('The game was Draw!')

        turn = 'X'
        print_board(the_board)


print('Thanks everybody for playing!')