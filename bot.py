import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import openai

# OpenAI API Key
openai.api_key = "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"  # Yahan apna OpenAI API key daalna

# Telegram Bot API Token
TELEGRAM_API_TOKEN = "7888770655:AAF6Ax3346v6ReqAk2rbIOwjxfz5YXCX0yA"  # Yahan apna Telegram bot token daalna

# Function to handle /start command
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hello! I am your AI assistant. Ask me anything!")

# Function to generate reply using OpenAI API
def generate_reply(message_text: str):
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=message_text,
            max_tokens=150
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error: {str(e)}"

# Function to handle messages
def handle_message(update: Update, context: CallbackContext):
    user_message = update.message.text
    ai_response = generate_reply(user_message)
    update.message.reply_text(ai_response)

# Main function
def main():
    updater = Updater(TELEGRAM_API_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)
    main()