import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

# Установка токена вашего бота
TOKEN = "6701923539:AAHUnaECT_EvqUY_jGVqXMFaXfT18-5nlNk"

# Инициализация бота
bot = telegram.Bot(token=TOKEN)
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Настройка логгирования
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

# Обработчик команды /start
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Привет! Добро пожаловать в наш фаст-фуд бот!")

# Обработчик команды /menu для показа меню
def menu(update, context):
    menu_text = "Меню:\n1. Гамбургер - $5\n2. Пицца - $10\n3. Фри - $3"
    context.bot.send_message(chat_id=update.effective_chat.id, text=menu_text)

# Обработчик команды /order для оформления заказа
def order(update, context):
    order_text = "Спасибо за заказ! Мы приступим к его обработке."
    context.bot.send_message(chat_id=update.effective_chat.id, text=order_text)

# Обработчик текстовых сообщений с заказом
def process_order(update, context):
    order_text = "Ваш заказ принят: " + update.message.text
    context.bot.send_message(chat_id=update.effective_chat.id, text=order_text)

# Обработчик неизвестных команд
def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Извините, я не понимаю эту команду.")

# Назначение обработчиков команд
start_handler = CommandHandler('start', start)
menu_handler = CommandHandler('menu', menu)
order_handler = CommandHandler('order', order)
unknown_handler = MessageHandler(Filters.command, unknown)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(menu_handler)
dispatcher.add_handler(order_handler)
dispatcher.add_handler(unknown_handler)

# Запуск бота
updater.start_polling()
updater.idle()
