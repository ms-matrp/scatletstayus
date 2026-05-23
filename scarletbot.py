import telebot
import requests
from bs4 import BeautifulSoup

TOKEN = "8314373495:AAGhoKY1m6AcMC23BmvYLkKv6XHKMnFjHks"
bot = telebot.TeleBot(TOKEN)


def get_status():
    url = "https://usescarlet.com"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")

    status = soup.select_one("h1.status svelte-1w0cweh")

    if status:
        return status.text.strip()

    return "Status not found"


@bot.message_handler(commands=['start'])
def start(message):
    status = get_status()

    bot.send_message(
        message.chat.id,
        f"🔥 Scarlet Status: {status}"
    )


print("Bot started")
bot.infinity_polling()
