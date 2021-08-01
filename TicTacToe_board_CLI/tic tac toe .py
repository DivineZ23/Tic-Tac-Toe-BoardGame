from IPython.display import clear_output
def display_board(board):
    clear_output()

    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])

def take_input():
    marker = ''
    while marker!='x'and marker!='o':
        marker = input('Player 1,choose x or o:   ')
    player1 = marker

    if player1 == 'x':
        player2 = 'o'
    else:
        player2 = 'x'
    return (player1,player2)

def place_marker(board,pos,marker):
    board[pos] = marker

def win_condition(board, mark):

    return ((board[1] == board[2] == board[3] == mark) or
    (board[4] == board[5] == board[6] == mark) or
    (board[7] == board[8] == board[9] == mark) or
    (board[1] == board[4] == board[7] == mark) or
    (board[2] == board[5] == board[8] == mark) or
    (board[3] == board[6] == board[9] == mark) or
    (board[1] == board[5] == board[9] == mark) or
    (board[3] == board[5] == board[7] == mark))



import random

def choose_first():
    toss=random.randint(0,1)

    if toss == 0:
        return 'player 1'
    else:
        return 'player 2'


def space_check(board,pos):

    return board[pos] == ' '


def full_board_check(board):

    for i in range(1,10):
        if space_check(board,i):
            return False

    return True



def player_choice(board):

    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        x = input('Choose a position: (1-9)')
        if x.isdigit() == False:
            break
        else:
            position = int(x)

    return position

def play_again():
    response = input('Do you want to play again? Enter (Y/N)')

    return response == 'Y'

print ('Tic Tac Toe')

while True:

    #setup everything
    play_board = [' ']*10
    player1_marker,player2_marker = take_input()

    turn = choose_first()
    print (f'{turn} Will go first')

    game_on = True

    while game_on:
        if turn == 'player 1':
            #show the board
            display_board(play_board)

            #choose a position
            position = player_choice(play_board)

            #place the marker on the postion
            place_marker(play_board,position,player1_marker)

            #check for win or tie
            if win_condition(play_board,player1_marker):

                display_board(play_board)
                print ('Player 1 won')
                game_on = False
            else:
                if full_board_check(play_board):
                    display_board(play_board)
                    print('Tie game')
                    game_on = False
                else:
                    turn = 'player 2'

        else:
            #show the board
            display_board(play_board)

            #choose a position
            position = player_choice(play_board)

            #place the marker on the postion
            place_marker(play_board,position,player2_marker)

            #check for win or tie
            if win_condition(play_board,player2_marker):

                display_board(play_board)
                print ('Player 2 won')
                game_on = False
            else:
                if full_board_check(play_board):
                    display_board(play_board)
                    print('Tie game')
                    game_on = False
                else:
                    turn = 'player 1'
    if not play_again():
        break
