import os
import telebot

TOKEN = '8091843967:AAEVnckah1n2jZDgoS5dTegIPkR2rZja68k'
bot = telebot.TeleBot(TOKEN)

SAVE_PATH = "videos"
os.makedirs(SAVE_PATH, exist_ok=True)

@bot.message_handler(content_types=['video', 'document'])
def handle_video(message):
    file_info = bot.get_file(message.video.file_id if message.content_type == 'video' else message.document.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    
    file_name = f"{message.chat.id}_{file_info.file_path.split('/')[-1]}"
    file_path = os.path.join(SAVE_PATH, file_name)
    
    with open(file_path, 'wb') as f:
        f.write(downloaded_file)
    
    bot.reply_to(message, f"Video qabul qilindi: {file_name}\nMen uni ko‘rib chiqaman.")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Salom! Menga video yuboring, men uni qabul qilaman.")

print("Bot ishga tushdi...")
bot.polling()