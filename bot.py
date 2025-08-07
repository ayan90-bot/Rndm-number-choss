import telebot
import os
import random
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['give'])
def send_random_number(message):
    number = random.randint(1, 10)
    bot.reply_to(message, f"🎲 Your number is: {number}")

print("🤖 Bot is running...")
bot.infinity_polling()
