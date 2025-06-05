import telebot
import requests

BOT_TOKEN = input("Enter your Telegram Bot Token: ")
API_URL = "https://ziddibeatz.serv00.net/gaali_api.php"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['gaali'])
def send_gaali(message):
    try:
        response = requests.get(API_URL)
        if response.status_code == 200:
            data = response.json()
            gaali_text = data.get("response", "").strip()
            if gaali_text:
                bot.reply_to(message, gaali_text)
            else:
                bot.reply_to(message, "Gaali not found in response.")
        else:
            bot.reply_to(message, "Failed to get gaali from API.")
    except Exception as e:
        bot.reply_to(message, f"Error occurred: {e}")

print("✅ Bot is running...")
bot.infinity_polling()
