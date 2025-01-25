import json
import telebot
from bot import bot

def lambda_handler(event, context):
    try:
        # Parse the incoming Telegram update
        update = telebot.types.Update.de_json(json.loads(event['body']))
        
        # Process the update
        bot.process_new_updates([update])
        
        return {
            'statusCode': 200,
            'body': json.dumps('OK')
        }
    except Exception as e:
        print(e)
        return {
            'statusCode': 500,
            'body': json.dumps('Error processing update')
        }
      
