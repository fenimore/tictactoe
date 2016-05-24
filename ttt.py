#!/usr/bin/env python
"""Tic Tac Toe

A python module for playing tic tac toe.

The MIT License (MIT)
Copyright (c) 2016 Fenimore Love

TODO:
Add Color output
    
Attributes:
board_size -- the amount of squares
squares -- the value of each square defaults empty or 0
squares_printed -- the user input choices 1 - board_size
squares_valid -- a list of possible valid inputs 1 - board_size
win_dict -- a dict of winning combinations (input: combos)
instructions -- welcome message for user
"""
import itertools, random


board_size = 9 

squares = [0 for x in range(0, board_size)]
squares_printed = [str(ind + 1) for ind, val in enumerate(squares)]
squares_valid = [int(x) for x in squares_printed]

win_dict = {
    '1': [(1, 2), (3, 8), (4, 8)], '2': [(4, 7), (0, 2)],
    '3': [(1, 0), (4, 6), (5, 8)], '4': [(0, 6), (4, 5)],
    '5': [(1, 7), (3, 5), (0, 8), (2, 6)],  # Middle square
    '6': [(4, 3), (2, 8)], '7': [(0, 3), (7, 8), (4, 2)],
    '8': [(6, 8), (4, 1)], '9': [(2, 5), (6, 7), (0, 4)],
    }

instructions = """
\n\n    *********\n    TicTacToe\n    *********\n\n
    Enter a number below to claim a square
    Enter q to quit\n
    Player 1 (Crosses) to move:
    """


def print_board(feedback):
    """Print board and message to user.

    This function is called for setup, moves,
    and gameover.

    Keyword arguments:
    feedback -- the message sent to player
    """
    print(feedback)
    print('    ' + squares_printed[0] + '|' + squares_printed[1] + '|' + squares_printed[2])
    print('    ' + '-----')
    print('    ' + squares_printed[3] + '|' + squares_printed[4] + '|' + squares_printed[5])
    print('    ' + '-----')
    print('    ' + squares_printed[6] + '|' + squares_printed[7] + '|' + squares_printed[8])


def ask_move():
    """Get user input and validate results.

    This function returns the entered move, 
    or 0 if input is other than 1-9 or taken.

    Raises:
    IndexError -- if move is below -8 or above 9
    ValueError -- if move is not an int
    """
    move = input('    Enter Next Move (single digit): ')
    try:
        if squares[int(move) - 1] is 0:  # Check for empty square
            if int(move) > 0:  # No negative numbers
                return int(move)
            else: 
                return 0  # Doesn't reprint board
        else:
            print_board('\n    WOOPS\n    That square is taken')
            return 0
    except: 
        if move == 'q':
            print('\n    quitting... Goodbye\n')
            quit()
        print_board('\n    WOOPS\n    Please enter a single digit: ')
        return 0


def make_move(move, player):
    """Take the valid move and update grid.

    This function updates squares, squares_printed, 
    and squares_valid value. It then checks for a 
    win and prints the board.
    
    Keyword arguments:
    move -- the 1-9 coordinates the user inputs
    player -- either 1 or 2, the value changed in squares
    """
    squares[move - 1] = player
    squares_valid.remove(move)
    if player == 1:
        squares_printed[move-1] = 'X'
    elif player == 2:
        squares_printed[move-1] = 'O'
    
    if check_victory(move):
        print_board('\n    Game Over')
        print('\n    Player ' + str(player) + ' Wins ')
        quit()
    else:
        print_board('\n    Player: ' + str(player) + ' has moved: ')


def check_victory(last_move):
    """Use last move as a key for winning combinations.

    This function accesses win_dict with last_move as key.
    It returns 1 or 2 according to the value of the square. 
    Otherwise it returns 0.

    Keyword arguments:
    last_move -- the move played most recently
    """
    for possible_wins in win_dict[str(last_move)]:
        if (squares[last_move - 1] 
            == squares[int(possible_wins[0])] 
            == squares[int(possible_wins[1])]):
            return squares[int(last_move) - 1]
    return 0


def computer_random(): 
    """Choose random square from squares_valid."""
    new_move = random.choice(squares_valid)
    return new_move


def computer_best():  # TODO: Add decision tree
    """Place move according to three possible openings"""
    # https://en.wikipedia.org/wiki/Tic-tac-toe#Strategy
    return 0


def play_tic_tac_toe(default_order):
    """Prompts a move until squares are filled.

    This function prints the instructions and
    takes user input. It loops until the squares of full
    and iterates player_order 1 and 2.
    
    Keyword arguments:
    order -- defaults to True, Crosses first
    """
    if default_order:
        player_order = itertools.cycle([1, 2])
    else:
        player_order = itertools.cycle([2, 1])
        
    print_board(instructions)
    for _ in range(len(squares)):
        while True:
            user_input = ask_move()
            if user_input:
                next_move = user_input
                break

        make_move(next_move, next(player_order))    
    else:
        print('\n    Cat\'s game (draw)\n')

def play_computer(easy):
    """Play against computer
    
    This function is the human vs computer
    mode. The human player goes first.
    
    Keyword arguments:
    easy -- True is using computer_random
    """
    if easy:
        player_order = itertools.cycle([2, 1])
        player = next(player_order)
        print_board(instructions)
        for _ in range(len(squares)):
            while True:
                if player == 2:
                    user_input = ask_move()
                    if user_input:
                        next_move = user_input
                        break
                elif player == 1:
                    next_move = computer_random()
                    break
    
            player = next(player_order)
            make_move(next_move, player)    
        else:
            print('\n    Cat\'s game (draw)\n')
    else:
        print('hard difficulty')


if __name__ == "__main__":
    """Play Tic Tac Toe
    
    The main thread offers choices to the user
    for the two modes available, computer or 
    human opponents.
    
    Options:
    human versus human -- choose player order
    human versus computer -- choose difficulty
    TODO: computer versus computer
    """
    mode = input('Play h - human or c - computer? ')
    if mode == 'h':
        order = input('Choose x or o to go first? ')
        if order == 'x':
            play_tic_tac_toe(True)
        elif order == 'o':
            play_tic_tac_toe(False)
    if mode == 'c':
        difficulty = input('Play e - easy or h - hard? ')
        if difficulty == 'e':
            play_computer(True)
        if difficulty == 'h':
            print('no hard mode yet')
    else:
        print('I don\'t understand your choice')
