import telebot
from telebot import types
import math


bot = telebot.TeleBot('YOUR_TOKEN')

s = []
def perevod(p):

    for i in p.split():
        if type(i) == str:
            try:
                s.append(int(i))
            except ValueError as e:
                s.append(i)
            

def korni(v):

    s.append(perevod(v))

    a = s[0]
    b = s[1]
    c = s[2]

    dis = ((b*b) - (4*a*c))
    sqrt_d = math.sqrt(abs(dis))

    x1 = ((-b + sqrt_d)/(2*a))
    x2 = ((-b - sqrt_d)/(2*a))

    if dis > 0:
        return ('Дискриминант:' + '\n' + str(dis) + '\n\n' + 'Два корня:' + '\n' + str(x1) + '\n' + str(x2))
    
    if dis == 0:
        return ('Дискриминант:' + '\n' + str(dis) + '\n\n' + 'Один корень:'+ '\n' + str(x1))
    
    else:
        return ('Дискриминант:' + '\n' + str(dis) + '\n\n' + 'Нет корней')
    


@bot.message_handler(commands=["start"])
def start(m):
    bot.send_message(m.chat.id, "Здравствуй, {0.first_name}! Меня зовут Арсений Альбертович, я бот математик. Поэтому, если тебе в падлу решать что-то, я тебе помогу. А вот еще что, я все также не люблю, когда меня обзывают. Ну, удачи в обучении, надеюсь я смогу помочь тебе)".format(m.from_user))
    perm1 = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("Создатели", url = 'https://vk.com/public216399744')
    perm1.add(button1)
    bot.send_message(m.chat.id, "Хей, если тебе интересно кто меня создал, нажми на кнопку и перейди по ссылке. А если хочешь следить за обновлением моих возможностей, подпишись, моему создателю будет очень приятно.)".format(m.from_user), reply_markup=perm1)
    perm2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button2 = types.KeyboardButton("Квадратные уравнения")
    perm2.add(button2)
    bot.send_message(m.chat.id, "Итак, выбери, что я буду решать", reply_markup=perm2)



@bot.message_handler(content_types=["text"])
def math_text(message):
    if message.text == "Спасибо":
        bot.send_message(message.chat.id, "Не за что, надеюсь скоро увидимся")
    elif message.text == "Квадратные уравнения":
        bot.send_message(message.chat.id, "Введи коэфиценты, и я скажу ответ")
    else:
        bot.send_message(message.chat.id, korni(message.text))

    

bot.polling(none_stop=True, interval=0)


'''
Авторы: Mersibo
'''