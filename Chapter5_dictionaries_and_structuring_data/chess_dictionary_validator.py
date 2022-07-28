import pprint
from unittest import result

pieces = ['rook','knight','bishop','queen','king', 'pawn']


def create_chess_board(pieces): # use this function to generate a new start board



    initial_chess_board = {}
    p = 0
    pi = 0
    for l in range(1,9,1):
        while p < 8:
            while pi < 6:
                for r in ['a','b','c','d','e','f','g','h']:
                    
                    if l == 1:
                        if p <= 2:
                            initial_chess_board.setdefault(f'{str(l)+r}','w'+pieces[pi]+str(1))
                            p += 1
                            pi += 1
                        elif 2 < p <= 4:
                            initial_chess_board.setdefault(f'{str(l)+r}','w'+pieces[pi])
                            p += 1
                            pi += 1
                        elif p > 4:
                            if pi > 4:
                                pi = 2
                            initial_chess_board.setdefault(f'{str(l)+r}','w'+pieces[pi]+str(2))
                            p += 1
                            pi -= 1
                            if pi < 0:
                                pi = 6
                    elif l == 2:
                        initial_chess_board.setdefault(f'{str(l)+r}','w'+pieces[5]+str(p+1))
                        p += 1
                        pi = 6
                    elif 2 < l < 7:
                        initial_chess_board.setdefault(f'{str(l)+r}','')
                        p += 1
                        pi = 6
                    elif l == 7:
                        initial_chess_board.setdefault(f'{str(l)+r}','b'+pieces[5]+str(p+1))
                        p += 1
                        pi = 6
                        
                    elif l == 8:
                        if p <= 2:
                            initial_chess_board.setdefault(f'{str(l)+r}','b'+pieces[pi]+str(1))
                            p += 1
                            pi += 1
                        elif 2 < p <= 4:
                            initial_chess_board.setdefault(f'{str(l)+r}','b'+pieces[pi])
                            p += 1
                            pi += 1
                        elif p > 4:
                            if pi > 4:
                                pi = 2
                            initial_chess_board.setdefault(f'{str(l)+r}','b'+pieces[pi]+str(2))
                            p += 1
                            pi -= 1
                            if pi < 0:
                                pi = 6
        p = 0
        pi = 0

    return initial_chess_board


the_board = {'1a': 'wrook', '1b': 'wknight', '1c': 'wbishop', '1d': 'wqueen', '1e': 'wking', '1f': 'wbishop', '1g': 'wknight', '1h': 'wrook',\
             '2a': 'wpawn', '2b': 'wpawn', '2c': 'wpawn', '2d': 'wpawn', '2e': 'wpawn', '2f': 'wpawn', '2g': 'wpawn', '2h': 'wpawn',\
             '3a': '', '3b': '', '3c': '', '3d': '', '3e': '', '3f': '', '3g': '', '3h': '',\
             '4a': '', '4b': '', '4c': '', '4d': '', '4e': '', '4f': '', '4g': '', '4h': '',\
             '5a': '', '5b': '', '5c': '', '5d': '', '5e': '', '5f': '', '5g': '', '5h': '',\
             '6a': '', '6b': '', '6c': '', '6d': '', '6e': '', '6f': '', '6g': '', '6h': '',\
             '7a': 'bpawn', '7b': 'bpawn', '7c': 'bpawn', '7d': 'bpawn', '7e': 'bpawn', '7f': 'bpawn', '7g': 'bpawn', '7h': 'bpawn',\
             '8a': 'brook', '8b': 'bknight', '8c': 'bbishop', '8d': 'bqueen', '8e': 'bking', '8f': 'bbishop', '8g': 'bknight', '8h': 'brook'}




def is_valid_chessBoard(board):

    count_positions = {}
    count_pieces= {}
    count_color_pieces = {}

    result = True

    

    for v in board.values(): # count pieces

        count_pieces.setdefault(v, 0)
        count_pieces[v] = count_pieces[v] + 1
        
        try:
            if v[0] == 'w':
                count_color_pieces.setdefault('w', 0)
                count_color_pieces['w'] = count_color_pieces['w'] + 1
            elif v[0] == 'b':
                count_color_pieces.setdefault('b',0)
                count_color_pieces['b'] = count_color_pieces['b'] + 1
        except Exception as e:
            pass

    

    for k in board.keys(): # count positions
        count_positions.setdefault(k, 0)
        count_positions[k] = count_positions[k] + 1

    if count_pieces['wking'] > 1 or count_pieces['bking'] > 1: # rule: 1 black king and 1 white king

        result = False
    
    elif count_color_pieces['b'] > 16 or count_color_pieces['w'] > 16: # rule: Each player can only have at most 16 pieces
        
        result = False
    
    elif count_pieces['bpawn'] > 8 or count_pieces['wpawn'] > 8: # rule: at most 8 pawns

        result = False
    else:
        
        for k in board.keys(): # rule: all pieces must be on a valid space from '1a' to '8h'; that is, a piece can’t be on space '9z'
            
            knumber = int(k[0])
            kletter = k[1]
            if knumber > 8:

                result = False
            elif kletter not in ['a','b','c','d','e','f','g','h']:
                
                result = False
                break
            else:

                result = True
    print(count_positions)
    #return result
    
    

 



print(is_valid_chessBoard(the_board))

#print(create_chess_board(pieces))