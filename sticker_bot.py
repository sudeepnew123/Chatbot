from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

# Sticker mapping
STICKER_REPLY_MAP = {
    '🙂': 'CAACAgUAAx0CXcbz-QLStdRoAn6b_qPTdIuYZdiWgmuUV1oDjAAC6xIAAq9ieVYWuQweDgmsBDYE',
    '😎': 'AAMCBQADGQEB8yIMaAnBKp5yDVnx2JLhvPHLWMXjpk8AAoMUAAKXCRlUjronykwj0yABAAdtAAM2BA',
    '😂': 'AAMCBQADGQEB8yIJaAnBJChCl-fNYzQP1pMkYmYg7nEAAmYOAAK_21hUkhWNpl1D75oBAAdtAAM2BA',
    '🥲': 'AAMCBQADGQEB8yIEaAnBHquthuOd9keXKNBk7kskLA0AAgMLAAIMTOBWLv-SzcSjbdkBAAdtAAM2BA',
    '❤️': 'AAMCBQADGQEB8yICaAnBHJVjW6thVE7TXD6iS3Y4oI4AAloMAAIXuLlUO602ukS2NssBAAdtAAM2BA',
    '😁': 'CAACAgUAAxkBAfMiOWgJwYLkmpbtb4BzIJuzT5LupLgoAAMWAAIFBRlX85jGPNPzh2o2BA',
    '😒': 'CAACAgUAAxkBAfMiQWgJwZWmuv4r664yvBIxplfDiZRRAALBFAACtSUZVxW0RaQzvfLONgQ'
}

# Your Telegram ID
OWNER_ID = 6356015122

async def handle_sticker(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.from_user.id != OWNER_ID:
        return

    sticker = update.message.sticker
    emoji = sticker.emoji

    if emoji in STICKER_REPLY_MAP:
        await update.message.reply_sticker(STICKER_REPLY_MAP[emoji])
    else:
        await update.message.reply_text("Sticker emoji not in list!")

if __name__ == '__main__':
    import os
    from dotenv import load_dotenv
    load_dotenv()

    TOKEN = os.getenv("BOT_TOKEN")

    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.STICKER, handle_sticker))

    print("Bot is running...")
    app.run_polling()