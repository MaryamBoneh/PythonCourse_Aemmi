import time
import colorama
import random
from colorama import Fore, Back, Style


colorama.init()

game = [
    ['_', '_', '_'],
    ['_', '_', '_'],
    ['_', '_', '_'],
]

counter = 0
start_time = time.time()

print(Fore.MAGENTA + 'please choose single player or two player game: \n 1- single player \n 2- two player')
oneORtwo = input()


def show():
    for i in range(3):
        for j in range(3):
            if game[i][j] == 'X':
                print(Fore.CYAN + game[i][j], end=' ')
            elif game[i][j] == 'O':
                print(Fore.GREEN + game[i][j], end=' ')
            else:
                print(Fore.WHITE + game[i][j], end=' ')
        print('')


def exit_program():
    end_time = time.time()
    print('time spent in the game: ', end_time - start_time)
    exit()


def check():
    if game[0][0] == game[1][1] == game[2][2]:

        if game[1][1] == 'X':
            if oneORtwo == '2':
                print(Fore.YELLOW + 'Player 1 is winner!')
            else:
                print(Fore.YELLOW + 'You are winner!')

        elif game[1][1] == 'O':
            if oneORtwo == '2':
                print(Fore.YELLOW + 'Player 2 is winner!')
            else:
                print(Fore.YELLOW + 'Computer is winner!')

        exit_program()

    elif game[2][0] == game[1][1] == game[0][2]:
        if game[1][1] == 'X':
            if oneORtwo == '2':
                print(Fore.YELLOW + 'Player 1 is winner!')
            else:
                print(Fore.YELLOW + 'You are winner!')

        elif game[1][1] == 'O':
            if oneORtwo == '2':
                print(Fore.YELLOW + 'Player 2 is winner!')
            else:
                print(Fore.YELLOW + 'Computer is winner!')

        exit_program()

    else:
        for i in range(3):
            if game[i][0] == game[i][1] == game[i][2] == 'X':
                if oneORtwo == '2':
                    print(Fore.YELLOW + 'Player 1 is winner!')
                else:
                    print(Fore.YELLOW + 'You are winner!')
                exit_program()

            elif game[i][0] == game[i][1] == game[i][2] == 'O':
                if oneORtwo == '2':
                    print(Fore.YELLOW + 'Player 2 is winner!')
                else:
                    print(Fore.YELLOW + 'Computer is winner!')
                exit_program()

            elif game[0][i] == game[1][i] == game[2][i] == 'X':
                if oneORtwo == '2':
                    print(Fore.YELLOW + 'Player 1 is winner!')
                else:
                    print(Fore.YELLOW + 'You are winner!')
                exit_program()

            elif game[0][i] == game[1][i] == game[2][i] == 'O':
                if oneORtwo == '2':
                    print(Fore.YELLOW + 'Player 2 is winner!')
                else:
                    print(Fore.YELLOW + 'Computer is winner!')
                exit_program()

    if counter == 9:
        print(Fore.CYAN + 'Drow!')
        exit_program()


show()

while True:
    if oneORtwo == '2':
        print(Fore.CYAN + '\n**** \t Player 1 \t **** ')
    else:
        print(Fore.CYAN + '\n**** \t You \t **** ')

    while True:
        row = int(input('row: '))
        col = int(input('col: '))

        if 0 <= row <= 2 and 0 <= col <= 2:
            if game[row][col] == '_':
                game[row][col] = 'X'
                counter += 1
                break
            else:
                print('Error!   this cell is not empty. please try again.')
        else:
            print('Error!   index out of range. please try again.')

    show()
    check()

    if oneORtwo == '2':
        print(Fore.GREEN + '\n**** \t Player 2 \t ****')
        while True:
            row = int(input('row: '))
            col = int(input('col: '))

            if 0 <= row <= 2 and 0 <= col <= 2:
                if game[row][col] == '_':
                    game[row][col] = 'O'
                    counter += 1
                    break
                else:
                    print('Error!   this cell is not empty. please try again.')
            else:
                print('Error!   index out of range. please try again.')

        show()
        check()

    elif oneORtwo == '1':
        print(Fore.GREEN + '\n**** \t Computer \t ****')
        while True:
            row = random.randint(0, 2)
            col = random.randint(0, 2)

            if 0 <= row <= 2 and 0 <= col <= 2:
                if game[row][col] == '_':
                    game[row][col] = 'O'
                    counter += 1
                    break

        show()
        check()
