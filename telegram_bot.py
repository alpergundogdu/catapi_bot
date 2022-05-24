#!/usr/bin/python3
import argparse
import logging
import telegram
from commands.cat import CatQueue, NAMES_IDS
from functools import partial
from telegram.ext import Updater, CommandHandler

logging.basicConfig(level=logging.WARNING,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

parser = argparse.ArgumentParser(description='Run a telegram bot.')
parser.add_argument('--token', required=True, help='API token for the telegram bot, retrieved from https://t.me/botfather')
args = parser.parse_args()

TOKEN = args.token

bot = telegram.Bot(token=TOKEN)
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher


def fetch_cat(cat_queue, update, context):
    update.message.reply_photo(cat_queue.get())


def fetch_breeds(update, context):
    update.message.reply_text(
        'Breeds: ' + ', '.join(['/' + name for name in sorted(NAMES_IDS.keys())]))


def add_command(dispatcher, cat_queue, commands):
    dispatcher.add_handler(CommandHandler(
        commands, partial(fetch_cat, cat_queue)))


def install_telegram(dispatcher):
    dispatcher.add_handler(CommandHandler(
        ['start', 'cat'], partial(fetch_cat, CatQueue(capacity=50))))
    for name, breed_id in NAMES_IDS.items():
        dispatcher.add_handler(CommandHandler(name, partial(
            fetch_cat, CatQueue(breeds=[breed_id], capacity=5))))
    dispatcher.add_handler(CommandHandler('breeds', fetch_breeds))


install_telegram(dispatcher)

if __name__ == "__main__":
    updater.start_polling()
