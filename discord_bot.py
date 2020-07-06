#!/usr/bin/python3
import discord
from commands.cat import CatQueue, NAMES_IDS

CLIENT_SECRET = '<Get client secret from https://discord.com/developers>'

cat_queue = CatQueue(capacity=50)

BREEDS = {}
for name, breed_id in NAMES_IDS.items():
    BREEDS[name] = CatQueue(breeds=[breed_id], capacity=5)

BREEDS_LOWER = dict([(name.lower(), name) for name in NAMES_IDS.keys()])


def add_whitespace(text):
    return "".join([(' ' + char if char.isupper() else char) for char in list(text)]).strip()


class CatApiBot(discord.Client):
    async def on_ready(self):
        pass

    async def on_message(self, message):
        if len(message.content) < 2:
            return
        message.content = message.content.lower()
        if message.content == '+cat':
            await message.channel.send('Here\'s your cat! ' + cat_queue.get())
        if message.content == '+breeds':
            await message.channel.send('Breeds: ' + ', '.join(['+' + name for name in NAMES_IDS.keys()]))
        if message.content == '+invite':
            await message.channel.send('Please use this link to invite me to your server: https://discord.com/oauth2/authorize?client_id=721475303452573726&scope=bot&permissions=2048')
        if message.content[0] == '+' and message.content[1:] in BREEDS_LOWER:
            await message.channel.send('Here\'s your ' + add_whitespace(BREEDS_LOWER[message.content[1:]]) + ' cat! ' + BREEDS[BREEDS_LOWER[message.content[1:]]].get())
        if message.content == '+help':
            await message.channel.send(
                'Thanks for using CatBot! ' +
                'Commands: ' +
                '+cat gives you a random cat image, ' +
                '+breeds lists available breeds (e.g. +siamese gives you a Siamese cat), ' +
                '+help shows this message. ' +
                'Any concerns, PM PuckNorris#5559 on Discord.')


client = CatApiBot()
client.run(CLIENT_SECRET)
