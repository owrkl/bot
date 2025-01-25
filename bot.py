import telebot

TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    if 'hello' in message.text.lower():
        bot.reply_to(message, "Hello! How can I help you today?")
    elif 'bye' in message.text.lower():
        bot.reply_to(message, "Goodbye! Have a great day!")
    else:
        bot.reply_to(message, "I'm a simple bot. I can only respond to 'hello' and 'bye'.")
        
