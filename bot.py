from flask import Flask
from threading import Thread
import telebot
import os
import random
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

# Dummy web server for Render's health check
app = Flask('')

@app.route('/')
def home():
    return "Bot is alive!"

def run():
    app.run(host='0.0.0.0', port=8080)

@bot.message_handler(commands=['give'])
def give_random_number(message):
    number = random.randint(1, 10)
    bot.reply_to(message, f"🎲 Your number is: {number}")

# Start dummy web server in thread
Thread(target=run).start()

# Start Telegram polling
bot.infinity_polling()
