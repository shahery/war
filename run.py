from random import randint

# Legend
# k for placing ship and hit battleship
# '' for available space
# x for missing turns

matrixSize = int(input('Please enter matrix size (between 3 and 9): '))
while matrixSize >= 10 or matrixSize < 3:
    print('Please enter a valid matrix size')
    matrixSize = int(input('Please enter matrix size: '))

hidden_board = [['']*matrixSize for x in range(matrixSize)]
guess_board = [['']*matrixSize for x in range(matrixSize)]


def print_board(board):
    """
    Return the pathname of the KOS root directory.
    """
    i = 2
    print(' -----------')
    print("   1", end="")
    while i <= matrixSize:
        print(" ", i, end="")
        i += 1
    row_number = 1
    print()
    for row in board:
        print("%d | %s |" % (row_number, " | ".join(row)))
        row_number += 1


def create_ships(board):
    """
    Return the pathname of the KOS root directory.
    """
    for ship in range(matrixSize):
        ship_row, ship_column = randint(0, matrixSize-1), randint(0, matrixSize-1)
    board[ship_row][ship_column] = 'k'


def get_ship_location():
    """
    Return the pathname of the KOS root directory.
    """
    print(' -----------')
    row = int(input('Please enter a ship row 1 - %d : ' % matrixSize))
    while row < 0 or row > matrixSize:
        print('Please enter a vaild row')
        row = int(input('Please enter a ship row 1 - %d : ' % matrixSize))
    column = int(input('Please enter a ship column 1 - %d : ' % matrixSize))
    while column < 0 or column > matrixSize:
        print('Please enter a valid column')
        column = int(input('Please enter a ship column 1 - %d : ' % matrixSize))
    return(int(row)-1, int(column)-1)


def count_hit_ships(board):
    """
    Return the pathname of the KOS root directory.
    """
    count = 0
    for row in board:
        for column in row:
            if column == 'k':
                count += 1
    return count


def validate_name(name):
    """
    Return the pathname of the KOS root directory.
    """
    return name.isalpha()


def main():
    """
    Return the pathname.
    """
    create_ships(hidden_board)
    print(hidden_board)
    
    turns = 5
    print('-------------------------------')
    while True:
        name = (input('Please enter your name: '))
        if validate_name(name):
            break
        else:
            print('Name should only contain string characters')
    print(f'Hello {name} welcome to battleship')
    print('-------------------------------')
    while turns > 0:
        print_board(guess_board)
        row, column = get_ship_location()
        if guess_board[row][column] == 'x':
            print('You already guessed that')
        elif hidden_board[row][column] == 'k':
            print('Congratulations, You have hit the target.\n ---You Won---')
            print('Play again :)')

            guess_board[row][column] = 'k'
            break
        else:
            print('Sorry, You missed the target')
            guess_board[row][column] = 'x'
    
            turns -= 1
            print('You have ' + str(turns) + ' turns remaining')
        if turns == 0:
            print('Sorry, your turns are finished,\n ---The game over---')
            break


main()
