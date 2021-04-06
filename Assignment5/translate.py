# -------------init---------------
print('Loading...')

try:
    f = open('Assignment5/translate.txt')

except Exception as e:
    print("error: ", e)
    exit()

big_text = f.read()
parts = big_text.split('\n')

words = []
i = 0

while i < len(parts):
    words.append({'english': parts[i], 'persian': parts[i+1]})
    i += 2

print('data loaded! \nwelcome dear user!')

# ------------process--------------


def addNewWord():
    english_text = input('please enter the english word: ')
    persian_text = input('please enter the persian word: ')

    words.append({'english': english_text, 'persian': persian_text})

    f = open('Assignment5/translate.txt', 'a')
    f.write('\n'+english_text)
    f.write('\n'+persian_text)
    f.close()

    print('Done!')
    menu()


def translationToPersian():
    user_text = input('please enter your text: ')
    user_words = user_text.split(' ')

    for i in range(len(user_words)):
        for j in range(len(words)):
            if words[j]['english'] == user_words[i]:
                print(words[j]['persian'], end=' ')
                break
        else:
            print(user_words[i], end=' ')
    menu()


def translationToEnglish():
    user_text = input('please enter your text: ')
    user_words = user_text.split(' ')

    for i in range(len(user_words)):
        for j in range(len(words)):
            if words[j]['persian'] == user_words[i]:
                print(words[j]['english'], end=' ')
                break
        else:
            print(user_words[i], end=' ')
    menu()


def menu():
    print('\n \n 1- add new word \n 2- translation english to persian \n 3- translation persian to english \n 4- exit')
    user_select = input('please enter the option you want: ')

    if user_select == '1':
        addNewWord()
    elif user_select == '2':
        translationToPersian()
    elif user_select == '3':
        translationToEnglish()
    else:
        exit()


menu()
