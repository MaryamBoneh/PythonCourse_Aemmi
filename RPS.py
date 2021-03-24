import random

items = ["Rock", "Paper", "Scissors"]
computer_score = 0
user_score = 0


while True:
    computer_select = random.choice(items)
    print('please select an item: \n 0- Rock \n 1- Paper \n 2- Scissors \n 3- Exit')

    if computer_score == 3:
            print('Computer Wins')
            break
    elif computer_score == 3:
        print('You Wins!!')
        break

    else:
        user_select = input()
        if user_select == '3':
            print('computer score is: ', computer_score,
                ' and user score is: ', user_score)
            break
        else:
            if computer_select == 'Rock':
                if user_select == '1':
                    print('excellent!!')
                    user_score += 1
                elif user_select == '2':
                    print('Oops!!')
                    computer_score += 1

            elif computer_select == 'Paper':
                if user_select == '2':
                    print('excellent!!')
                    user_score += 1
                elif user_select == '0':
                    print('Oops!!')
                    computer_score += 1

            elif computer_select == 'Scissors':
                if user_select == '0':
                    print('excellent!!')
                    user_score += 1
                elif user_select == '1':
                    print('Oops!!')
                    computer_score += 1

            print('computer score is: ', computer_score,
                ' and user score is: ', user_score, '\n')
