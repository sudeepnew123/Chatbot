from flask import Flask, request
import telegram
import os

TOKEN = os.getenv("7888770655:AAF6Ax3346v6ReqAk2rbIOwjxfz5YXCX0yA")
BOT = telegram.Bot(token=TOKEN)

# Sirf Sudip ke liye bot kaam karega
ALLOWED_USER_ID = 6356015122

# Sticker mapping (emoji ya file_unique_id : reply sticker ID)
STICKER_REPLY_MAP = {
    '😢': 'CAACAgUAAxkBAAEF4c9mL0nRhstickerID_example1',
    '😂': 'CAACAgUAAxkBAAEF4dFmHappySticker_example2',
    '❤️': 'CAACAgUAAxkBAAEF4eNmHeartSticker_example3',
    # Add more emojis or file_unique_ids here
}

app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), BOT)
    if update.message and update.message.sticker:
        user_id = update.message.from_user.id
        chat_id = update.message.chat_id
        sticker = update.message.sticker

        if user_id == ALLOWED_USER_ID:
            reply_sticker = None
            if sticker.emoji in STICKER_REPLY_MAP:
                reply_sticker = STICKER_REPLY_MAP[sticker.emoji]
            elif sticker.file_unique_id in STICKER_REPLY_MAP:
                reply_sticker = STICKER_REPLY_MAP[sticker.file_unique_id]

            if reply_sticker:
                BOT.send_sticker(
                    chat_id=chat_id,
                    sticker=reply_sticker,
                    reply_to_message_id=update.message.message_id
                )
    return 'ok'