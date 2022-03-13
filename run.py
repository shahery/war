from random import randint
# Legend
# x for placing ship and hit battleship
# '' for available space

hidden_board = [['']*8 for x in range(8)]
guess_board = [['']*8 for x in range(8)]
letters_to_numbers = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 
                      'e': 4, 'f': 5, 'g': 6, 'h': 7}


def print_board(board):
    print('a b c d e f g h')
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|" .join(row)))
        row_number += 1


def create_ships(board):
    for ship in range(5):
        ship_row, ship_column = randint(0, 7), randint(0, 7)
    while board[ship_row][ship_column] == 'x':
        ship_row, ship_column = randint(0, 7), randint(0, 7)
    board[ship_row][ship_column] = 'x'


def get_ship_location():
    row = input('Please enter a ship row 1-8: ')
    while row not in '12345678':
        print('Please enter a vaild row')
        row = input('Please  enter a ship row 1-8: ')
    column = input('Please enter a ship column a-h: ')
    while column not in 'abcdefgh':
        print('Please enter a valid column')
        column = input('Please enter a ship column a-h: ')
    return(int(row)-1, letters_to_numbers[column])


def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == 'x':
                count += 1
    return count


create_ships(hidden_board)
turns = 5
while turns > 0:
    name = input('Please enter your name: ')
    print(f"Hello {name} Welcome to battleship")
    print_board(guess_board)
    row, column = get_ship_location()
    if guess_board[row][column] == '-':
        print('You already guessed that')
    elif hidden_board[row][column] == 'x':
        print('Congratulations, You have hit the battleship')
        guess_board[row][column] = 'x'
        turns -= 1
    else:
        print('Sorry, You missed')
        guess_board[row][column] = '-'
        turns -= 1
    if count_hit_ships(guess_board) == 5:
        print('congratulations, You have sunk all the battleships')
        break
    print('You have ' + str(turns) + ' turns remaining')
    if turns == 0:
        print('Sorry, you ran out of turns, The game over')
        break




