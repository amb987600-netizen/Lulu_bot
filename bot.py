import telebot
import random
import requests
import time
import os
from datetime import datetime
from telebot import types

# التوكنات والمفاتيح
TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN', "8316405971:AAHH9i26CERO16K8bNj740CptRx0-93m8-Y")
DEVELOPER_ID = 1254154279
DEVELOPER_NAME = "أحمد"

# تهيئة البوت
bot = telebot.TeleBot(TELEGRAM_TOKEN)

# شخصية لولو
class LuluPersonality:
    def __init__(self):
        self.responses = {
            'greeting': [
                "آهلاً ياقمر! 🌸 إزيك؟",
                "يا هلا بيك! 🌟 نورت!",
                "إزيك ياحبيبي؟ 🍯 أخبارك إيه؟",
                "آهلاً يانجم! 🤗 إشتقنا ليك!"
            ],
            'lulu_called': [
                "🌸 إيه ياقمر؟ إزيك؟",
                "💫 نعمتي؟ قولي لي",
                "🌹 حاضر يا قلبي!",
                "💖 إزيك ياحبيبي؟"
            ]
        }
    
    def get_greeting(self):
        return random.choice(self.responses['greeting'])
    
    def get_lulu_response(self):
        return random.choice(self.responses['lulu_called'])

lulu = LuluPersonality()

# الرد على جميع الرسائل
@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    text = message.text.strip()
    
    if text.startswith('/'):
        return
    
    if any(word in text.lower() for word in ['لولو', 'lulu']):
        response = lulu.get_lulu_response()
        bot.reply_to(message, response)
        return
    
    elif any(word in text.lower() for word in ['مرحبا', 'اهلا', 'السلام']):
        greeting = lulu.get_greeting()
        bot.reply_to(message, greeting)
        return
    
    elif random.random() < 0.5:
        responses = ["واو! 🌸", "يا جميل! 💫", "معلش ياقلبى 🎀"]
        bot.reply_to(message, random.choice(responses))

# أمر البداية
@bot.message_handler(commands=['start'])
def start_command(message):
    welcome_text = f"""
🌸 *مرحباً ياقمر! أنا لولو* 💖

*مطوري:* {DEVELOPER_NAME}

*جربي تكتبي:* 
لولو
أو: مرحبا
    """
    bot.reply_to(message, welcome_text, parse_mode='Markdown')

# تشغيل البوت
def start_bot():
    while True:
        try:
            print("🚀 بوت لولو شغال على Render!")
            bot.polling(none_stop=True, interval=1, timeout=60)
        except Exception as e:
            print(f"❌ خطأ: {e}")
            time.sleep(15)

if __name__ == "__main__":
    start_bot()
