import telebot

# ⚠️ Yahan apna asli Bot Token dalein
BOT_TOKEN = '8997723330:AAHaFDzFezZ27jsoV60m-kgCUq0KbqV'
bot = telebot.TeleBot(BOT_TOKEN)

# ⚠️ Yahan apne target group/channel ki Chat ID dalein
TARGET_CHAT_ID = -1004410908316 

@bot.message_handler(content_types=['photo', 'video', 'document', 'audio', 'voice'])
def forward_media(message):
    try:
        # Bot media ko aapke target channel/group me forward kar dega
        bot.forward_message(chat_id=TARGET_CHAT_ID, from_chat_id=message.chat.id, message_id=message.message_id)
        print("Media successfully forwarded!")
    except Exception as e:
        print(f"Error aaya bhai: {e}")

print("Bot chalu ho gaya hai...")
bot.infinity_polling()
