import telebot
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

TOKEN = "8314373495:AAGhoKY1m6AcMC23BmvYLkKv6XHKMnFjHks"

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )

    driver.get("https://usescarlet.com")

    status = driver.find_element(
        By.CLASS_NAME,
        "status svelte-1w0cweh"
    ).text

    bot.send_message(
        message.chat.id,
        f"🔥 Scarlet Status: {status}"
    )

    driver.quit()


bot.infinity_polling()
