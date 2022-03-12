from random import randint

hidden_board=[['']*8 for x in range(8)]
guess_board=[['']*8 for x in range(8)]
letters_to_numbers={'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
def print_board(board):
    print('abcdefgh')
    row_number=1
    for row in board:
        print("%d|%s|" %(row_number,"|".join(row)))
        row_number +=1


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
                count +=1
    return count


create_ships(hidden_board)
print(hidden_board)



