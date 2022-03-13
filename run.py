from random import randint
# Legend
# k for placing ship and hit battleship
# '' for available space
# x for missing turns

hidden_board = [['']*6 for x in range(6)]
guess_board = [['']*6 for x in range(6)]
letters_to_numbers = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4,
                      'f': 5}


def print_board(board):
    print('a b c d e f')
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1


def create_ships(board):
    for ship in range(5):
        ship_row, ship_column = randint(0, 5), randint(0, 5)
    while board[ship_row][ship_column] == 'k':
        ship_row, ship_column = randint(0, 5), randint(0, 5)
    board[ship_row][ship_column] = 'k'


def get_ship_location():
    row = input('Please enter a ship row 1-6: ')
    while row not in '123456':
        print('Please enter a vaild row')
        row = input('Please  enter a ship row 1-6: ')
    column = input('Please enter a ship column a-f: ')
    while column not in 'abcdef':
        print('Please enter a valid column')
        column = input('Please enter a ship column a-f: ')
    return(int(row)-1, letters_to_numbers[column])


def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == 'k':
                count += 1
    return count


create_ships(hidden_board)
print(hidden_board)
turns = 5
name = input('Please enter your name: ')
print(f"Hello {name} welcome to battleship")
while turns > 0:
    print_board(guess_board)
    row, column = get_ship_location()
    if guess_board[row][column] == 'x':
        print('You already guessed that')
    elif hidden_board[row][column] == 'k':
        print('Congratulations, You have hit the battleship')
        print('Play again :)')
        guess_board[row][column] = 'k'
        break
    else:
        print('Sorry, You missed')
        guess_board[row][column] = 'x'
        turns -= 1
    print('You have ' + str(turns) + ' turns remaining')
    if turns == 0:
        print('Sorry, you ran out of turns, The game over')
        break




