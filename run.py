from random import randint
# Legend
# k for placing ship and hit battleship
# '' for available space
# x for missing turns

hidden_plank = [['']*6 for x in range(6)]
guess_plank = [['']*6 for x in range(6)]
letters_to_numbers = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4,
                      'f': 5}


def print_plank(plank):
    print('a b c d e f')
    row_number = 1
    for row in plank:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1


def create_ships(plank):
    for ship in range(5):
        ship_row, ship_column = randint(0, 5), randint(0, 5)
    while plank[ship_row][ship_column] == 'k':
        ship_row, ship_column = randint(0, 5), randint(0, 5)
    plank[ship_row][ship_column] = 'k'


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


def count_hit_ships(plank):
    count = 0
    for row in plank:
        for column in row:
            if column == 'k':
                count += 1
    return count


create_ships(hidden_plank)
print(hidden_plank)
turns = 5
name = input('Please enter your name: ')
print(f"Hello {name} welcome to battleship")
while turns > 0:
    print_plank(guess_plank)
    row, column = get_ship_location()
    if guess_plank[row][column] == 'x':
        print('You already guessed that')
    elif hidden_plank[row][column] == 'k':
        print('Congratulations, You have hit the battleship')
        print('Play again :)')
        guess_plank[row][column] = 'k'
        break
    else:
        print('Sorry, You missed')
        guess_plank[row][column] = 'x'
        turns -= 1
    print('You have ' + str(turns) + ' turns remaining')
    if turns == 0:
        print('Sorry, you ran out of turns, The game over')
        break




