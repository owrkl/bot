from flask import Flask
import os
app = Flask(__name__)
if __name__ == "__main__"
	port = int(os.environ.get("PORT",10000))
  app.run(host="0.0.0.0", port=port)
import telebot

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot = telebot.TeleBot('7464314334:AAFTLYZ2UJdIAfsjOuhNklcGfR934XbxsDA')

# Dictionary of word-response pairs
responses = {
    'hello': 'Hi there!',
    'how are you': 'I'm doing great, thanks for asking!',
    'bye': 'Goodbye! Have a great day!',
    'help': 'I'm a simple bot. Try saying hello, how are you, or bye.',
    'weather': 'I'm not a weather bot, but I hope it's sunny where you are!',
    'thanks': 'You're welcome!',
    'joke': 'Why don't scientists trust atoms? Because they make up everything!',
    'music': 'I love all kinds of music! What's your favorite genre?',
    'food': 'Talking about food makes me hungry. What's your favorite dish?',
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
