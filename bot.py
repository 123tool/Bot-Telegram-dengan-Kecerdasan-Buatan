
                        import telebot

# Create a new instance of the TeleBot class
bot = telebot.TeleBot("YOUR_TELEGRAM_BOT_TOKEN")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    """
    Handler function for the '/start' and '/help' commands.

    Parameters:
    - message: telebot.types.Message
        The message object received from the user.

    Returns:
    - None
    """

    # Send a welcome message to the user
    bot.reply_to(message, "Welcome to the AI Telegram Bot!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    """
    Handler function for all other messages.

    Parameters:
    - message: telebot.types.Message
        The message object received from the user.

    Returns:
    - None
    """

    # Echo the user's message back to them
    bot.reply_to(message, message.text)

# Start the bot
bot.polling()
                    
