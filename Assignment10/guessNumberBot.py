import telebot
import random

bot = telebot.TeleBot("________YOUR TOKEN________")
number = random.randint(1, 20)
score = 6
print('score', score)


def newGame():
    global number
    global score
    number = random.randint(1, 20)
    score = 6


@bot.message_handler(commands=['start'])
def say_wellcom(message):
    bot.send_message(message.chat.id, f'خوش اومدي🌺{message.from_user.first_name} از 1 تا 20 يه عدد رو حدس بزن 😉')
    bot.send_message(message.chat.id, 'با دستور /new می تونی بازی جدید بیاری')


bottuns = telebot.types.ReplyKeyboardMarkup(row_width=1)
btn = telebot.types.KeyboardButton('بازي جديد')
bottuns.add(btn)


@bot.message_handler(commands=['new'])
def new_game(message):
    bot.send_message(message.chat.id, 'بازی جدید؟', reply_markup=bottuns)


@bot.message_handler(func=lambda message: True)
def send_normal_message(message):
    if message.text.isnumeric():
        global score
        print('user: ', message.text, 'goal: ', number, 'score: ', score)
        
        if int(message.text) == number:
            bot.reply_to(message,  f'تو برنده شدي🎉🎁')
            newGame()
            bot.send_message(
                message.chat.id, 'از 1 تا 20 يه عدد رو حدس بزن')

        elif int(message.text) > number:
            score -= 1
            if score == 0:
                bot.send_message(message.chat.id, 'نتونستی تشخیص بدی بسکو😒 امتیازت تموم شد. بریم یه بازی جدید')
                newGame()
                bot.send_message(message.chat.id, 'از 1 تا 20 يه عدد رو حدس بزن')
            else:
                bot.reply_to(message, 'برو پايين تر')
                bot.send_message(message.chat.id, score*'♥️')

        elif int(message.text) < number:
            score -= 1                
            if score == 0:
                bot.send_message(message.chat.id, 'نتونستی تشخیص بدی بسکو😒 امتیازت تموم شد. بریم یه بازی جدید')
                newGame()
                bot.send_message(message.chat.id, 'از 1 تا 20 يه عدد رو حدس بزن')
            else:
                bot.reply_to(message, 'برو بالاتر')
                bot.send_message(message.chat.id, score*'♥️')
    else:
        if message.text == 'بازي جديد' or message.text == 'بازی جدید':
            newGame()
            bot.send_message(message.chat.id, 'از 1 تا 20 يه عدد رو حدس بزن')
        else:
            bot.reply_to(message, 'نمی فهمم چی میگی!')


bot.polling()
