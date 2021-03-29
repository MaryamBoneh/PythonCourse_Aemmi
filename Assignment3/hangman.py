import random

words_bank = ['tree', 'stAr', 'Sajjad', 'Maryam' 'apple', 'python', 'MOON']
score = 10
true_letters = []
word = random.choice(words_bank)

while True:

    for c in word:
        if (c in true_letters) or (chr(int(ord(c))+32) in true_letters) or (chr(int(ord(c))-32) in true_letters):
            print(c, end='')
        else:
            print('_ ', end='')

    char = input('\n please enter a letter: ')

    if (char in word) or (chr(int(ord(char))+32) in word) or (chr(int(ord(char))-32) in word):
        true_letters.append(char)
    else:
        score -= 1

    print('score= ', score)

    if (len(true_letters) == len(word)):
        print('You Win !!!')
        break
    if (score == 0):
        print('Game Over')
        break
