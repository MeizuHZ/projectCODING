from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, filters, MessageHandler


key_token = "6305844992:AAFgZUZ8ugTKynKN_cYQvsTXz9QWToQ8msY"
user_bot = "@simplebotigs"

async def  start_command(update: Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Gunakan /help untuk menampilkan apa aja tentang pemilik bot ini")
    
async def  help_command(update: Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Kirim pesan: siapa kamu, idol, song, university, ig, school, quotes ")
    await update.message.reply_text("play game: gunting, batu, kertas ")




async def  text_massage(update: Update, context:ContextTypes.DEFAULT_TYPE):
    text_diterima : str = update.message.text
    print(f"Pesan diterima : {text_diterima}")
    text_lwr_diterima = text_diterima.lower()
    if 'school' in text_lwr_diterima:
        await update.message.reply_text("https://youtu.be/66WgrAoHcEI?si=R4_mV-8HBkn80mML")
    elif 'idol' in text_lwr_diterima:
        await update.message.reply_text("tiwiiii : https://youtu.be/wQuccIp6BNM?si=oVjWaSuyZL5xottK")
        await update.message.reply_text("Maenggg : https://youtu.be/0vWnkbkpYUI?si=t4tTYYBBQrBQ-vYq")
    elif 'university' in text_lwr_diterima:
        await update.message.reply_text("idaman banget : https://youtu.be/dy48ygPbU5o?si=qJK9cKSCpj7SsKiW")
    elif 'song' in text_lwr_diterima:
        await update.message.reply_text("https://youtu.be/qmpmUxWwOyA?si=SlFJH3FTtWmQXDjT")
        await update.message.reply_text("https://youtu.be/QKnooWemRfQ?si=Der7ebCxA910ZVwX")
    elif 'ig' in text_lwr_diterima:
        await update.message.reply_text("jangan lupa follow ya :) https://www.instagram.com/tadaohz_/?utm_source=ig_web_button_share_sheet&igshid=OGQ5ZDc2ODk2ZA==")
    elif 'siapa kamu' in text_lwr_diterima:
        await update.message.reply_text("nama saya adalah Hafiz zulfikar ahmad, saya berasal dari pelambang")
    elif 'quotes' in text_lwr_diterima:
        await update.message.reply_text("People who cant throw something important away can never hope to change anything")
        await update.message.reply_text("A life that lives without doing anything is the same as a slow death.")
    elif 'gunting' in text_lwr_diterima:
        await update.message.reply_text("batu")
    elif 'batu' in text_lwr_diterima:
        await update.message.reply_text("kertas")
    elif 'kertas' in text_lwr_diterima:
        await update.message.reply_text("gunting")
    else:
        await update.message.reply_text("bot tidak mengerti")


async def photo_message(update: Update, context:ContextTypes.DEFAULT_TYPE):
    return await update.message.reply_text("Gambar kamu bagus")
        
async def  error(update: Update, context:ContextTypes.DEFAULT_TYPE):
    print(f"error... : {context.error}")


if __name__ == '__main__':
    print("Mulai")
    app = Application.builder().token(key_token).build()
    #COMMAND :
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    #MESSAGE:
    app.add_handler(MessageHandler(filters.TEXT, text_massage))
    app.add_handler(MessageHandler(filters.PHOTO, photo_message))
    #error :
    app.add_error_handler(error)
    #polling :
    app.run_polling(poll_interval=1)
