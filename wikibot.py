import telebot, wikipedia, re
from telebot import types

bot = telebot.TeleBot('YOUR_TOKEN')

wikipedia.set_lang("ru")

def getwiki(s):
    try:
        ny = wikipedia.page(s)
        wikitext=ny.content[:1000]
        wikimas = wikitext.split('.')
        wikimas = wikimas[:-1]
        wikitext2 = ''
        
        for x in wikimas:
            if not('==' in x):
                if len((x.strip()))>3:
                    wikitext2 = wikitext2 + x + '.'
            else:
                break
        
        wikitext2 = re.sub('\([^()]*\)',  '', wikitext2)
        wikitext2 = re.sub('\([^()]*\)',  '', wikitext2)
        wikitext2 = re.sub('\{[^\{\}]*\}', '', wikitext2)

        return wikitext2
    except Exception as e:
        return 'Я пока не знаю ответ на этот вопрос'

@bot.message_handler(commands=["start"])
def start(m):
    bot.send_message(m.chat.id, "Здравствуй, {0.first_name}! Меня зовут Всезнайка, и я знаю все. Я помогу тебе, если ты что-то не знаешь, пиши в любое время, я всегда свободен).".format(m.from_user))
    perm1 = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("Создатели", url = 'https://vk.com/public216399744')
    perm1.add(button1)
    bot.send_message(m.chat.id, "Хей, если тебе интересно кто меня создал, нажми на кнопку и перейди по ссылке. А если хочешь следить за обновлением моих возможностей, подпишись, моему создателю будет очень приятно.)".format(m.from_user), reply_markup=perm1)
    bot.send_message(m.chat.id, 'Отправь мне любое слово, и я скажу его значение')

@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, getwiki(message.text))

bot.polling(none_stop=True, interval=0)


'''
Авторы: Mersibo
'''


