import traceback
import telebot
from config import TOKEN, currency
from extensions import Convertor, APIException

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = "Введи команду в следующем формате: \n <Какую валюту переводите> <в какую валюту переводите> <сумма>.\n \
    Список валют /list"
    bot.reply_to(message, text)


@bot.message_handler(commands=['list'])
def values(message: telebot.types.Message):
    text = '\n'.join('{} - {}'.format(key, val) for key, val in currency.items())

    bot.reply_to(message, f'Доступные валюты: \n{text}')

@bot.message_handler(content_types=['text'])
def converter(message: telebot.types.Message):
    values = message.text.split()
    try:
        if len(values) != 3:
            raise APIException('Неверное количество параметров!')
        answer = Convertor.get_price(values[0], values[1], values[2])
    except APIException as e:
        bot.reply_to(message, f"Ошибка в команде:\n{e}")
    except Exception as e:
        traceback.print_tb(e.__traceback__)
        bot.reply_to(message, f"Неизвестная ошибка:\n{e}")
    else:
        bot.reply_to(message, answer)


bot.polling()
