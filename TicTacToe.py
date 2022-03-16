from secrets import choice
from turtle import position
from IPython.display import clear_output


def display_board(board):
    print(' '+board[7]+' | '+board[8]+' | '+board[9])
    print('-----------')
    print(' '+board[4]+' | '+board[5]+' | '+board[6])
    print('-----------')
    print(' '+board[1]+' | '+board[2]+' | '+board[3])


board = [' ']*10
board[0] = '$'

print(display_board(board))


def player_input():
    pass


player1 = 'x'
player2 = 'o'


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    return((board[7] == board[8] == board[9] == mark) or (board[4] == board[5] == board[6] == mark) or (board[1] == board[2] == board[3] == mark) or
           (board[7] == board[4] == board[1] == mark) or (board[8] == board[5] == board[2] == mark) or (board[9] == board[6] == board[3] == mark) or
           (board[1] == board[5] == board[9] == mark) or (board[1] == board[5] == board[9] == mark))


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
        else:
            return True
            #board is full


def player_choice(board):
    position = 0
    while position not in range(1, 11) or not space_check(board, position):
        position = int(input('Choose a position: (1-9)'))
        return position


def replay():
    choice = input("Play again? Enter yes or no")
    return choice == 'yes'


turn = "Player 1"


print("Welcome to Tic Tac Toe")

while True:
    play_game = input("Ready to play? y or n: ")
    if play_game == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        display_board(board)
        position = player_choice(board)
        if turn == "Player 1":
            place_marker(board, player1, position)

            if win_check(board, player1,):
                display_board(board)
                print('Player 1 has won')
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print("Tie Game")
                    game_on = False
                else:
                    turn = "Player 2"
        else:

            place_marker(board, player2, position)

            if win_check(board, player2,):
                display_board(board)
                print('Player 2 has won')
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print("Tie Game")
                    game_on = False
                else:
                    turn = "Player 1"
