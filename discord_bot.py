#!/usr/bin/python3
import argparse
import discord
from commands.cat import CatQueue, NAMES_IDS

parser = argparse.ArgumentParser(description='Run a discord bot.')
parser.add_argument('--token', type=str,
                    help='API token for the discord bot, retrieved from https://discord.com/developers')
parser.add_argument('--client_id', type=str,
                    help='Client ID of the bot, retrieved from https://discord.com/developers')
parser.add_argument('--creator', type=str,
                    help='Discord ID of the creator of this bot, that\'s you!')
args = parser.parse_args()

CLIENT_ID = args.client_id
API_TOKEN = args.token
CREATOR = args.creator

INVITE_LINK = f'https://discord.com/oauth2/authorize?client_id={CLIENT_ID}&scope=bot&permissions=2048'

cat_queue = CatQueue()

BREED_QUEUES = {}
for name, breed_id in NAMES_IDS.items():
    BREED_QUEUES[name] = CatQueue(breeds=[breed_id])

BREEDS_LOWER = dict([(name.lower(), name) for name in NAMES_IDS.keys()])

CAT_EMOJIS = ['🐱', '🙀', '😾', '😿', '😼', '😻', '😺', '😹', '😸', '😽', '🐅', '🐈']


def add_whitespace(text):
    return "".join([(' ' + char if char.isupper() else char) for char in list(text)]).strip()


def get_cat_breed(breed):
    breed = BREEDS_LOWER[breed]
    name = add_whitespace(breed)
    image = BREED_QUEUES[breed].get()
    return 'Here\'s your ' + name + ' cat! ' + image


class CatApiBot(discord.Client):
    async def on_ready(self):
        pass

    async def on_message(self, message):
        if len(message.content) < 2 or message.content[0] != '+':
            return
        command = message.content[1:].lower()
        if command == 'cat' or command in CAT_EMOJIS:
            await message.channel.send('Here\'s your cat! ' + cat_queue.get())
        if command == 'catbreeds':
            await message.channel.send('Breeds: ' + ', '.join(['+' + name for name in NAMES_IDS.keys()]))
        if command == 'catinvite':
            await message.channel.send(f'Please use this link to invite me to your server: {INVITE_LINK}')
        if command in BREEDS_LOWER:
            await message.channel.send(get_cat_breed(command))
        if command == 'catservers':
            await message.channel.send("# of servers: " + str(len(self.guilds)))
        if command == 'help':
            await message.channel.send(
                'Thanks for using CatBot! \n' +
                'Commands: \n' +
                '+cat gives you a random cat image \n' +
                '+catBreeds lists available breeds (e.g. +siamese gives you a Siamese cat) \n' +
                '+catInvite to invite me to another server \n' +
                '+help shows this message \n' +
                f'Any concerns, PM {CREATOR} on Discord.')


intents = discord.Intents.default()
intents.message_content = True

client = CatApiBot(intents=intents)
client.run(API_TOKEN)
