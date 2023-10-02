from googletrans import Translator
import gtts
import os
import telebot
from telebot import types

bot = telebot.TeleBot('YOUR_TOKEN')

@bot.message_handler(commands=['start'])
def send_start(m):
    bot.send_message(m.chat.id, "Здравствуй, {0.first_name}! Меня зовут Дмiтро Ткачук, я бот переводчик на украинский.)".format(m.from_user))
    perm1 = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("Создатели", url = 'https://vk.com/public216399744')
    perm1.add(button1)
    bot.send_message(m.chat.id, "Хей, если тебе интересно кто меня создал, нажми на кнопку и перейди по ссылке. А если хочешь следить за обновлением моих возможностей, подпишись, моему создателю будет очень приятно.)".format(m.from_user), reply_markup=perm1)
    perm2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button2 = types.KeyboardButton("Русский")
    button3 = types.KeyboardButton("Українська мова")
    perm2.add(button2, button3)
    bot.send_message(m.chat.id, "Выбери исходный язык", reply_markup=perm2)

@bot.message_handler(content_types='text')
def on_translate(message):
    translator = Translator()
    lang = translator.detect(message.text)
    print(message, lang)

    if message == 'Русский':
        transed = translator.translate(message.text, sfr='ru', dest='uk')
    
        voice = gtts.gTTS(transed.text)
        voice.save(transed.text + ".mp3")
        bot.reply_to(message, transed.text)
        bot.send_audio(message.chat.id, audio=open(transed.text + ".mp3", "rb"))
        os.remove(transed.text + ".mp3")
    
    elif message == 'Українська мова':
        transed = translator.translate(message.text, sfr='uk', dest='ru')
    
        voice = gtts.gTTS(transed)
        voice.save(transed + ".mp3")
        bot.reply_to(message, transed)
        bot.send_audio(message.chat.id, audio=open(transed + ".mp3", "rb"))
        os.remove(transed + ".mp3")
    
    else:
        bot.reply_to(message, "Я вас не понял")


if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            print("ошибка:" + str(e))
