from flask import Flask
import os
import telebot

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot = telebot.TeleBot('7464314334:AAFTLYZ2UJdIAfsjOuhNklcGfR934XbxsDA')

# Dictionary f word-response pairs
responses = {
    'hello': 'Hi there!',
    'how are you': 'Im doing great, thanks for asking!',
    'bye' : 'Goodbye! Have a great day!',
    'help': 'Im a simple bot. Try saying hello, how are you, or bye.',
    'weather': 'Im not a weather bot, but I hope its sunny where you are!',
    'thanks': 'Youre welcome!',
    'joke': 'Why dont scientists trust atoms? Because they make up everything!',
    'music': 'I love all kinds of music! Whats your favorite genre?',
    'food': 'Talking about food makes me hungry. Whats your favorite dish?',
    'weekend': 'Weekends are the best! Any exciting plans?'
}

@bot.message_handler(func=lambda message: True)
def respond_to_message(message):
    text = message.text.lower()
    
    for word, response in responses.items():
        if word in text:
            bot.reply_to(message, response)
            return
    
    # If no matching word is found
    bot.reply_to(message, "I'm not sure how to respond to that. Try saying 'help' for some options.")

# Start the bot
bot.polling()
