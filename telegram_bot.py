#!/usr/bin/python3
import argparse
import logging
from commands.cat import CatQueue, NAMES_IDS
from functools import partial
from telegram.ext import CommandHandler, ApplicationBuilder

logging.basicConfig(level=logging.WARNING,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

parser = argparse.ArgumentParser(description='Run a telegram bot.')
parser.add_argument('--token', required=True,
                    help='API token for the telegram bot, retrieved from https://t.me/botfather')
args = parser.parse_args()

TOKEN = args.token


async def fetch_cat(cat_queue, update):
    await update.message.reply_photo(cat_queue.get())


async def fetch_breeds(update):
    await update.message.reply_text(
        'Breeds: ' + ', '.join(['/' + name for name in sorted(NAMES_IDS.keys())]))


def install_telegram(application):
    application.add_handler(CommandHandler(
        ['start', 'cat'], partial(fetch_cat, CatQueue(capacity=50))))
    for name, breed_id in NAMES_IDS.items():
        application.add_handler(CommandHandler(
            name, partial(fetch_cat, CatQueue([breed_id]))
        ))
    application.add_handler(CommandHandler('breeds', fetch_breeds))


if __name__ == "__main__":
    application = ApplicationBuilder().token(TOKEN).build()

    install_telegram(application)

    application.run_polling()
