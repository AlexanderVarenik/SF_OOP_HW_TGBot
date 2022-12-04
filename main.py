import json
import requests
import telebot

TOKEN = '5960801501:AAFwzNQAbsibCnLSHJDJsZ8_uG5U1QYwWhc'

bot = telebot.TeleBot(TOKEN)

keys = {
    'доллар': "USD",
    'евро': 'EUR',
}
@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Чтобы начать работу, введите команду боту в следующем формате:\n"название валюты \
"в какую валюту перевести" \
"количество валюты"\nУвидеть список всех доступных валют: /values'
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты'
    for key in keys.keys():
        text = '\n'.join((text, key,))
    bot.reply_to(message, text)

@bot.message_handler(func=lambda m: True)
def values(message: telebot.types.Message):
        quote, base, amount = message.text.lower().split(' ')
        s = f'https://anyapi.io/api/v1/exchange/convert?base={keys[base]}&to={keys[quote]}&amount={amount}&apiKey=ll0va71c56gmh5hpb5tqn8fpmt3gnstog9f1le0ubvrtpenvdv7otg'
        r = requests.get(f'https://anyapi.io/api/v1/exchange/convert?base={keys[base]}&to={keys[quote]}&amount={amount}&apiKey=ll0va71c56gmh5hpb5tqn8fpmt3gnstog9f1le0ubvrtpenvdv7otg')
        text = json.loads(r.content)['converted']
        bot.send_message(message.chat.id, text)

bot.polling()