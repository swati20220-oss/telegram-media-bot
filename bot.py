import threading
from flask import Flask
import telebot

# ---- YAHAN SE NAYA CODE SHURU HAI (REPLIT KO ZINDA RAKHNE KE LIYE) ----
app = Flask('')

@app.route('/')
def home():
    return "Bot is alive and running!"

def run_web_server():
    app.run(host='0.0.0.0', port=8080)

# Web server ko alag thread me chalu karenge taaki bot bhi chalta rahe
t = threading.Thread(target=run_web_server)
t.start()
# ---- NAYA CODE YAHAN KHATAM HAI ----


# ⚠️ Yahan tumhara asli Bot Token pehle se dala hai
BOT_TOKEN = '8997723330:AAHaFDzFezZ27jsoV60m-kgCUq0KbqVsXV4'
bot = telebot.TeleBot(BOT_TOKEN)

# ⚠️ Yahan tumhari target group/channel ki Chat ID pehle se dali hai
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
